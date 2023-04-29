from dataclasses import replace

from controllers.base_controller import BaseController
from game import logic
from models.game_models import Move, Position, Path


class LWalk(BaseController):
    current_position: Position
    actor_path: Path = []

    def __init__(self):
        self.current_position = replace(logic.get_actor_starting_position())
        self.actor_path.append(self.current_position)

    def move(self) -> Move:
        # go down and then go left
        next_position = Position(
            x=self.current_position.x, y=self.current_position.y + 1
        )
        _move = Move(self.current_position, next_position)
        if not logic.is_move_valid(_move):
            next_position.x = self.current_position.x + 1
            next_position.y = self.current_position.y
            if not logic.is_move_valid(_move):
                raise Exception("Can't move")

        self.current_position = next_position
        self.actor_path.append(self.current_position)
        return _move

    def get_current_position(self) -> Position:
        return self.current_position

    def get_actor_path(self) -> Path:
        return self.actor_path
