from enum import Enum


class Result(Enum):
    WHITE_WIN = "1-0"
    DRAWN = "0.5-0.5"
    BLACK_WIN = "0-1"
    WIN = 1
    DRAW = 0.5
    LOSS = 0
    NONE = ""