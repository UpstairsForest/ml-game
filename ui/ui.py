from typing import Any

import pygame

from models.game_models import Board, Path, Square
from ui.config import (
    dis_x,
    dis_y,
    step,
    red,
    green,
    yellow,
    white,
    background_color,
    gray,
    brown,
)


class UI:
    display: Any

    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((dis_x, dis_y))

    def draw(self, board: Board, actor_path: Path, failed_to_move=False):
        if failed_to_move:
            actor_color = brown
        else:
            actor_color = white
        for i, row in enumerate(board):
            for j, square in enumerate(row):
                if square == Square.START:
                    color = green
                elif square == Square.END:
                    color = red
                elif square == Square.COIN:
                    color = yellow
                else:
                    color = background_color
                pygame.draw.rect(
                    self.display, color=color, rect=[j * step, i * step, step, step]
                )

        for square in actor_path[:-1]:
            pygame.draw.rect(
                self.display,
                color=gray,
                rect=[step * square.x, step * square.y, step, step],
            )
        pygame.draw.rect(
            self.display,
            color=actor_color,
            rect=[step * actor_path[-1].x, step * actor_path[-1].y, step, step],
        )
        pygame.display.update()

    @staticmethod
    def check_if_terminated() -> bool:
        """Check and close UI if terminated"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                return True
