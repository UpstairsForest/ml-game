import random
from typing import List

from config import n_tiles, n_coins, board_width
from models.game_models import Board, Square, Move

_temp: List[Square] = (n_coins * [Square.COIN]) + ((n_tiles - 2 - n_coins) * [Square.EMPTY])
random.shuffle(_temp)
_temp = [Square.START] + _temp + [Square.END]

_board: Board = [_temp[i*board_width:i*board_width+board_width] for i in range(board_width)]


def get_board() -> Board:
    return _board


def update_actor_position(move: Move):
    _board[move.start.y][move.start.x] = Square.EMPTY
    _board[move.end.y][move.end.x] = Square.ACTOR
