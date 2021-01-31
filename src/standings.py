from typing import Dict, List

from texttable import Texttable

from src.pairing import Pairing
from src.pairing import Result
from src.player import PlayerList
from src.tiebreak import sonneborn_berger, direct_encounter, number_wins, number_blacks, buchholz


class Standings:
    def __init__(self, name: str, round: int, players: PlayerList, pairings: Dict[int, List[Pairing]]):
        self.name = name
        self.round = round
        self.players = players
        self.pairings = pairings
        self.tiebreaks = {}
        self.table = []
        self.sort_by_points()

    def sort_by_points(self):
        for r, ps in self.pairings.items():
            for p in ps:
                if p.result == Result.WHITE_WIN:
                    p.player_white.points += 1
                if p.result == Result.DRAW:
                    p.player_white.points += 0.5
                    p.player_black.points += 0.5
                if p.result == Result.BLACK_WIN:
                    p.player_black.points += 1

        self.players.sort()

        for player in self.players.players:
            self.table.append([player.name, 'WIP', player.pretty_points(), 'DE', 'SB', '#B'])

    def add_tiebreak(self, name: str, relevance: int) -> None:
        if name == 'Sonneborn-Berger':
            self.tiebreaks[relevance] = (name, sonneborn_berger)
        elif name == 'Direct encounter':
            self.tiebreaks[relevance] = (name, direct_encounter)
        elif name == 'number wins':
            self.tiebreaks[relevance] = (name, number_wins)
        elif name == 'Games with Black':
            self.tiebreaks[relevance] = (name, number_blacks)
        elif name == 'buchholz':
            self.tiebreaks[relevance] = (name, buchholz)
        else:
            raise Exception('{0}: Unknown tiebreak criterion!'.format(name))

    def calculate_standing(self) -> None:

        pass

    def __str__(self):
        table = Texttable(max_width=0)
        table.set_deco(Texttable.HEADER)
        table.set_precision(1)

        header_row = ['Place', 'Name', 'Games', 'Points']
        for v in self.tiebreaks.values():
            header_row.append(v[0])
        table.header(header_row)

        col_alignments = []
        cols = len(self.table[0]) + 1
        for c in range(cols):
            col_alignments.append('c')
        table.set_cols_align(col_alignments)

        for rank, player in enumerate(self.table):
            cur_row = [rank + 1]
            for entry in player:
                cur_row.append(entry)
            table.add_row(cur_row)

        return table.draw()
