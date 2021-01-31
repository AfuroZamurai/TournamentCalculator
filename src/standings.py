from typing import Dict

from src.player import Player
from src.player import PlayerList


class Standings:
    def __init__(self, name: str, round: int, players: PlayerList):
        self.name = name
        self.round = round
        self.players = players
        self.tiebreaks = {}
        self.table = []

    def add_tiebreak(self, name: str, tiebreak: Dict) -> None:
        self.tiebreaks[name] = tiebreak

    def calculate_standing(self) -> None:
        pass

    def __str__(self):
        table = '{0} Standings after round {1}\n'.format(self.name, self.round)
        table += '--------------------------------------------------\n'
        table += 'Place |       Name       | Games | Points | '

        for k, _ in self.tiebreaks.items():
            table += ' {0} |'.format(k)

        table += '\n--------------------------------------------------\n'

        for rank, player in enumerate(self.table):
            table += '  {0}  '.format(rank)
            for entry in player:
                table += '  {0}  '.format(entry)

        return table
