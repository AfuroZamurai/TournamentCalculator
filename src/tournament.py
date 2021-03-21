from typing import List, Dict

from src.pairing import Pairing
from src.player import PlayerList
from src.standings import Standings


class Tournament:
    def __init__(self, name: str, players: PlayerList, rounds: int, tiebreaks: List[str], pairings: Dict[int, List[Pairing]]):
        self.name = name
        self.players = players
        self.rounds = rounds
        self.tiebreaks = tiebreaks
        self.pairings = pairings

    def calculate_standings(self) -> Standings:
        standings = Standings(self.name, len(self.pairings), self.players, self.pairings)
        for i, tiebreak in enumerate(self.tiebreaks):
            standings.add_tiebreak(tiebreak, i + 1)
        standings.calculate_standing()
        return standings
