import copy
import random
from typing import List

from config import n_tiles, n_coins, board_width
from models.game_models import Board, Square, Move


class BoardManager:
    _starting_board: Board
    _current_board: Board

    def __init__(self):
        _temp: List[Square] = (n_coins * [Square.COIN]) + (
            (n_tiles - 2 - n_coins) * [Square.EMPTY]
        )
        random.shuffle(_temp)
        _temp = [Square.START] + _temp + [Square.END]

        self._starting_board = [
            _temp[i * board_width : i * board_width + board_width]
            for i in range(board_width)
        ]
        self._current_board = copy.deepcopy(self._starting_board)

    def get_starting_board(self) -> Board:
        return copy.deepcopy(self._starting_board)

    def get_current_board(self) -> Board:
        return self._current_board

    def update_actor_position(self, move: Move):
        self._current_board[move.start.y][move.start.x] = Square.EMPTY
        self._current_board[move.end.y][move.end.x] = Square.ACTOR
