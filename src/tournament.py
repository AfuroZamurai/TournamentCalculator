from typing import List, Dict

from src.pairing import Pairing
from src.player import PlayerList
from src.standings import Standings


class Tournament:
    def __init__(self, players: PlayerList, rounds: int, tiebreaks: List[str], pairings: Dict[int, List[Pairing]]):
        self.players = players
        self.rounds = rounds
        self.tiebreaks = tiebreaks
        self.pairings = pairings

    def calculate_standings(self) -> Standings:
        # TODO: decide on way to calculate this
        return Standings(self.players)
