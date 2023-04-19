from typing import List

import pygame.draw

from config import green, red, gray, step, white
from controllers.base_controller import Position


def _color_from_value(value):
    if value > 0:
        return green
    if value < 0:
        return red
    return gray


class Board:
    board: List[List[int]]

    def __init__(self, display, board_data: List[List[int]]):
        self.display = display
        self.board = board_data
        self.actor_position = Position(x=0, y=0)

    def draw(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                pygame.draw.rect(self.display, color=_color_from_value(value),
                                 rect=[step // 2 + j * step, step // 2 + i * step, step, step])
        pygame.draw.rect(self.display, color=white,
                         rect=[step // 2 + step * self.actor_position.x + 2 * step,
                               step // 2 + step * self.actor_position.y + 2 * step, step,
                               step])
        pygame.display.update()

    def update_actor_position(self, position: Position):
        self.actor_position = position
