from typing import List, Dict

from src.result import Result


class Player:
    def __init__(self, elo: int, name: str):
        """
        A PLayer is always part of a tournament and holds information about itself.
        The information can be personal (like name and possibly age, nationality and son on) or general, like points scored.
        :param elo: The Elo rating of this player at the time the tournament is played
        :param name: The full name of the player in the form first name last name
        """
        self.elo = elo
        self.name = name
        self.points: float = 0.0
        self.opponents: Dict[Player, List[Result]] = {}
        self.num_blacks = 0
        self.num_wins = 0

    def pretty_points(self):
        if self.points.is_integer():
            return str(int(self.points))
        else:
            return '{0:.1f}'.format(self.points)

    def add_opponent(self, opponent, result):
        if opponent.name not in self.opponents:
            self.opponents[opponent.name] = [result]
        else:
            self.opponents[opponent.name].append(result)

    def calculate_wins(self):
        for k, v in self.opponents.items():
            for result in v:
                if result == Result.WIN:
                    self.num_wins += 1

    def __str__(self):
        return self.name

    def __lt__(self, other):
        return self.points < other.points

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(repr(self))


class PlayerList:
    def __init__(self, players: List[Player]):
        self.players = players

    def sort(self):
        self.players.sort(reverse=True)

    def __getitem__(self, item: str):
        for player in self.players:
            if item == player.name:
                return player

        return None
