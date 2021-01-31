from typing import List

from player import Player


class Tournament:
    def __init__(self, players: List[Player], rounds: int):
        self.players = players
        self.rounds = rounds
