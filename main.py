import pygame

from controllers.base_controller import BaseController
from controllers.trivial_ai import TrivialAI
from ui.board import Board
from config import (
    dis_x,
    dis_y, fps, board_data,
)

pygame.init()
clock = pygame.time.Clock()
display = pygame.display.set_mode((dis_x, dis_y))

controller: BaseController = TrivialAI()
board: Board = Board(display, board_data)

board.draw()
game_over = False
while not game_over:
    next_move = controller.next_move()
    if next_move:
        board.update_actor_position(controller.get_current_position())
        board.draw()
    clock.tick(fps)
