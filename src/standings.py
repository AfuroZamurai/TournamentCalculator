from collections import OrderedDict
from typing import Dict, List, Optional

from texttable import Texttable

from src.pairing import Pairing
from src.result import Result
from src.player import PlayerList
from src.tiebreak import sonneborn_berger, direct_encounter, number_wins, number_blacks, buchholz


class Standings:
    def __init__(self, name: str, round: int, players: PlayerList, pairings: Dict[int, List[Pairing]]):
        self.name = name
        self.round = round
        self.players = players
        self.pairings = pairings
        self.tiebreaks = OrderedDict()
        self.table: List[Dict] = []

    def sort_by_points(self):
        for r, ps in self.pairings.items():
            for p in ps:
                white = p.player_white
                black = p.player_black

                if p.result == Result.WHITE_WIN:
                    white.points += 1
                    white.add_opponent(black, Result.WIN)
                    black.add_opponent(white, Result.LOSS)
                if p.result == Result.DRAWN:
                    white.points += 0.5
                    black.points += 0.5
                    white.add_opponent(black, Result.DRAW)
                    black.add_opponent(white, Result.DRAW)
                if p.result == Result.BLACK_WIN:
                    black.points += 1
                    white.add_opponent(black, Result.LOSS)
                    black.add_opponent(white, Result.WIN)

        self.players.sort()

        for player in self.players.players:
            elements = {
                'name': player.name,
                'round': self.round,
                'points': player.pretty_points()
            }
            for tiebreak in self.tiebreaks.values():
                elements[tiebreak[0]] = 'N/A'
            self.table.append(elements)

    def add_tiebreak(self, name: str, relevance: int) -> None:
        if name == 'Sonneborn-Berger':
            self.tiebreaks[relevance] = (name, sonneborn_berger, 't')
        elif name == 'Direct encounter':
            self.tiebreaks[relevance] = (name, direct_encounter, 't')
        elif name == 'number wins':
            self.tiebreaks[relevance] = (name, number_wins, 'i')
        elif name == 'Games with Black':
            self.tiebreaks[relevance] = (name, number_blacks, 'i')
        elif name == 'buchholz':
            self.tiebreaks[relevance] = (name, buchholz, 't')
        else:
            raise Exception('{0}: Unknown tiebreak criterion!'.format(name))

    def sort_criterions(self):
        self.tiebreaks[-1] = ('points', None)
        self.tiebreaks.move_to_end(-1, last=False)
        return lambda x: [x[t[0]] for t in self.tiebreaks.values()]

    def sort_by_tiebreaks(self):
        self.table.sort(key=self.sort_criterions(), reverse=True)
        del self.tiebreaks[-1]

    def calculate_standing(self) -> None:
        self.sort_by_points()
        for relevance, tiebreak in self.tiebreaks.items():
            self.table = tiebreak[1](self.table, self.players, self.pairings, relevance)

        self.sort_by_tiebreaks()

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

        col_dtypes = ['i', 't', 'i', 't']
        for tiebreak in self.tiebreaks.values():
            col_dtypes.append(tiebreak[2])
        table.set_cols_dtype(col_dtypes)

        for rank, player in enumerate(self.table):
            cur_row = [rank + 1]
            for entry in player.values():
                cur_row.append(entry)
            table.add_row(cur_row)

        return table.draw()
