from abc import ABC

from models.game_models import Position, Path, Move


class BaseController(ABC):
    def move(self) -> Move:
        raise NotImplemented

    def get_current_position(self) -> Position:
        raise NotImplemented

    def get_actor_path(self) -> Path:
        raise NotImplemented
