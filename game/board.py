import copy
import random
from typing import List, Optional

from config import n_tiles, n_coins, board_width
from models.game_models import Board, Square, Move, Position


class BoardManager:
    _starting_board: Board
    _current_board: Board
    _failed_to_move: bool = False

    def __init__(self):
        self.reset()

    def get_actor_ending_position(self) -> Position:
        for y, row in enumerate(self._starting_board):
            for x, square in enumerate(row):
                if square == Square.END:
                    return Position(x=x, y=y)
        raise Exception("did not find game_end position")

    def has_game_ended(self, actor_position: Position):
        ending_position = self.get_actor_ending_position()
        if actor_position.x == ending_position.x and actor_position.y == ending_position.y:
            return True
        return False

    def get_starting_board(self) -> Board:
        return copy.deepcopy(self._starting_board)

    def get_current_board(self) -> Board:
        return self._current_board

    def update_actor_position(self, move: Optional[Move]):
        if move:
            self._current_board[move.start.y][move.start.x] = Square.EMPTY
            self._current_board[move.end.y][move.end.x] = Square.ACTOR
            self._failed_to_move = False
        else:
            self._failed_to_move = True

    def reset(self):
        _temp: List[Square] = (n_coins * [Square.COIN]) + (
                (n_tiles - 1 - n_coins) * [Square.EMPTY]
        ) + [Square.END]
        random.shuffle(_temp)

        self._starting_board = [
            _temp[i * board_width: i * board_width + board_width]
            for i in range(board_width)
        ]
        self._current_board = copy.deepcopy(self._starting_board)

    def failed_to_move(self) -> bool:
        return self._failed_to_move
