import random

from controllers.lwalk import LWalk
from game import logic
from models.game_models import Move, Position, Path


class RandomWalk(LWalk):
    current_position: Position
    actor_path: Path = []

    def move(self) -> Move:
        def random_adjacent_tile() -> Position:
            direction = random.randint(0, 3)
            if direction == 0:
                return Position(
                    x=self.current_position.x - 1, y=self.current_position.y
                )
            if direction == 1:
                return Position(
                    x=self.current_position.x + 1, y=self.current_position.y
                )
            if direction == 2:
                return Position(
                    x=self.current_position.x, y=self.current_position.y + 1
                )
            if direction == 3:
                return Position(
                    x=self.current_position.x, y=self.current_position.y - 1
                )

        _move = Move(self.current_position, random_adjacent_tile())
        while not logic.is_move_valid(_move):
            _move.end = random_adjacent_tile()

        self.current_position = _move.end
        self.actor_path.append(self.current_position)
        return _move
