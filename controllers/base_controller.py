from dataclasses import dataclass
from enum import Enum
from typing import Optional

from abc import ABC


class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)


@dataclass
class Position:
    x: int
    y: int


class BaseController(ABC):

    def next_move(self) -> Optional[Direction]:
        """Return next move if it has been made yet"""
        raise NotImplemented

    def get_current_position(self) -> Position:
        raise NotImplemented
