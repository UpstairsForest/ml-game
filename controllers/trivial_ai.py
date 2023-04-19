from typing import List, Optional

from controllers.base_controller import BaseController, Direction, Position


class TrivialAI(BaseController):
    board: List[List[int]]

    def next_move(self) -> Optional[Direction]:
        pass

    def get_current_position(self) -> Position:
        raise NotImplemented
