import sys
import time
from typing import Optional

from controllers.base_controller import BaseController

from controllers.random_walk import RandomWalk
from controllers.the_abominable_0 import TheAbominable0
from game import logic
from game.board import BoardManager
from config import (
    game_end_delay,
    frame_delay,
)
from ui.ui import UI


def exit_smoothly():
    exit()


def reset():
    board_manager.reset()
    controller.reset()


ui: Optional[UI] = None
if "--no-ui" not in sys.argv:
    ui = UI()

board_manager = BoardManager()
# controller: BaseController = LWalk()
controller: BaseController = TheAbominable0(board_manager)


# in case the abomination gets stuck
step_limit = 50
step = 0
while True:
    try:
        if step >= step_limit:
            reset()
            step = 0
        step += 1

        board_manager.update_actor_position(controller.move())
        if ui:
            ui.draw(
                board=board_manager.get_current_board(),
                actor_path=controller.get_actor_path(),
            )
            if ui.check_if_terminated():
                exit_smoothly()

        if board_manager.has_game_ended(controller.get_current_position()):
            if ui:
                time.sleep(game_end_delay)
            reset()
            step = 0
        # elif ui:
        #     time.sleep(frame_delay)
    except Exception as e:
        print(e)
        reset()
        step = 0
