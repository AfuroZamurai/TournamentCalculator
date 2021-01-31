from typing import List

from src.player import Player


class Tournament:
    def __init__(self, players: List[Player], rounds: int, tiebreaks: List[str]):
        self.players = players
        self.rounds = rounds
        self.tiebreaks = tiebreaks
