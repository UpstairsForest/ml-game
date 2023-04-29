import numpy as np

from config import board_width
from models.game_models import Move, Position, Path, Board, Square


def get_actor_starting_position() -> Position:
    return Position(x=0, y=0)


def get_actor_ending_position() -> Position:
    return Position(x=board_width - 1, y=board_width - 1)


def is_move_valid(move: Move):
    if not abs(move.start.x - move.end.x) + abs(move.start.y - move.end.y) == 1:
        return False
    if (move.end.x >= board_width) or (move.end.y >= board_width) or (move.end.x < 0) or (move.end.y < 0):
        return False
    return True


def has_game_ended(actor_position: Position):
    ending_position = get_actor_ending_position()
    if actor_position.x == ending_position.x and actor_position.y == ending_position.y:
        return True
    return False


def rate_result(actor_path: Path, starting_board: Board):
    # + for coins
    # - for stepping on one square more than once
    # ~ path length
    raise NotImplemented


def rate_move(move: Move, current_board: Board):
    # closer to goal is better
    # move-distance is the same, so direction is the only thing that matters
    x, y = None, None
    for y, row in enumerate(current_board):
        for x, square in enumerate(row):
            if square == Square.END:
                break
    if not x or not y:
        raise Exception("failed to find game_end")
    # scalar product
    prod = np.dot(
        [move.end.x - move.start.x, move.end.y - move.start.y],  # actor_start to actor_end vector
        [x - move.start.x, y - move.start.y],  # actor_start to game_end vector
    )
    # normalize
    return prod / np.abs(prod)
