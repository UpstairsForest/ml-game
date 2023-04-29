from dataclasses import dataclass
from enum import Enum
from typing import List


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Move:
    start: Position
    end: Position


class Square(Enum):
    START = "START"
    END = "END"
    EMPTY = "EMPTY"
    COIN = "COIN"
    ACTOR = "ACTOR"


Board = List[List[Square]]
Path = List[Position]
