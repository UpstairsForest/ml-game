import numpy as np

from config import board_width
from models.game_models import Move, Position, Path, Board, Square


def get_actor_starting_position() -> Position:
    x, y = np.random.choice([i for i in range(board_width)], size=2)
    return Position(x=x, y=y)


def is_move_valid(move: Move):
    if not abs(move.start.x - move.end.x) + abs(move.start.y - move.end.y) == 1:
        return False
    if (
        (move.end.x >= board_width)
        or (move.end.y >= board_width)
        or (move.end.x < 0)
        or (move.end.y < 0)
    ):
        return False
    return True


def rate_result(actor_path: Path, starting_board: Board):
    # + for coins
    # - for stepping on one square more than once
    # ~ path length
    raise NotImplemented


def rate_move(move: Move, current_board: Board):
    # closer to goal is better
    # move-distance is the same, so direction is the only thing that matters
    x, y = None, None
    for i, row in enumerate(current_board):
        for j, square in enumerate(row):
            if square == Square.END:
                x, y = j, i
    if not x or not y:
        raise Exception("failed to find game_end")
    # scalar product
    v1 = [
        move.end.x - move.start.x,
        move.end.y - move.start.y,
    ]  # actor_start to actor_end vector
    v2 = [x - move.start.x, y - move.start.y]  # actor_start to game_end vector
    prod = np.dot(v1, v2)
    # normalize
    return prod / (np.linalg.norm(v1) * np.linalg.norm(v2))
