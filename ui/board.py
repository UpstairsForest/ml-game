from typing import List

import pygame.draw

from config import green, red, gray, step
from controllers.base_controller import Position


class Board:
    board: List[List[int]]

    def __init__(self, display, board_data: List[List[int]]):
        self.display = display
        self.board = board_data

    def draw(self):
        for i, row in enumerate(self.board):
            for j, value in enumerate(row):
                pygame.draw.rect(self.display, color=self._color_from_value(value), rect=[step//2 + j*step,step//2 + i*step, step, step])
        pygame.display.update()

    def update_actor_position(self, position: Position):
        raise NotImplemented

    def _color_from_value(self, value):
        if value > 0:
            return green
        if value < 0:
            return red
        return gray
