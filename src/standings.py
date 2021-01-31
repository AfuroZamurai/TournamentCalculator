from typing import List

from src.player import Player
from src.player import PlayerList


class Standings:
    def __init__(self, players: PlayerList):
        self.players = players
        self.tiebreaks = {}

    def add_tiebreak(self, name, tiebreak):
        self.tiebreaks[name] = tiebreak

    def __str__(self):
        return 'Not implemented yet'
