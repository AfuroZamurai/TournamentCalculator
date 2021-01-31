from enum import Enum

from src.player import Player


class Result(Enum):
    WHITE_WIN = "1-0"
    DRAW = "0.5-0.5"
    BLACK_WIN = "0-1"


class Pairing:
    def __init__(self, player_white: Player, player_black: Player, result: Result = None):
        self.player_white = player_white
        self.player_black = player_black
        self.result = result

    def __str__(self):
        return '{0} - {1}: {2}'.format(self.player_white, self.player_black, self.result.value)


if __name__ == '__main__':
    p1 = Player(2823, 'Fabiano Caruana')
    p2 = Player(2862, 'Magnus Carlsen')
    pairing = Pairing(p1, p2)
    pairing.result = Result.DRAW

    print(pairing)
