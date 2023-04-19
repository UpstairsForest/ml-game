from typing import List

import pygame

from controllers.base_controller import Position
from ui.squares import Square


class Board:
    display: pygame.Surface
    board: List[List[Square]]

    def __init__(self, display: pygame.Surface, board_data: List[List[int]]):
        self.display = display
        self.board = [[Square(value) for value in row] for row in board_data]

    def draw(self):
        raise NotImplemented

    def update_actor_position(self, position: Position):
        raise NotImplemented
