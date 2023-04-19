import random
from typing import Optional

from controllers.base_controller import BaseController, Direction, Position


class TrivialAI(BaseController):
    x: int = 2
    y: int = 2

    def next_move(self) -> Optional[Direction]:
        direction = random.choice([direction for direction in Direction])
        self.y += direction.value[0]
        self.x += direction.value[1]
        return direction

    def get_current_position(self) -> Position:
        return Position(x=self.x, y=self.y)
