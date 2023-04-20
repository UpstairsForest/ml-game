import sys
import time
from typing import Optional

from controllers.base_controller import BaseController
from controllers.lwalk import LWalk
from controllers.random_walk import RandomWalk
from game import logic
from game.board import BoardManager
from config import (
    game_end_delay, frame_delay,
)
from ui.ui import UI


def exit_smoothly():
    # todo: save data and such
    exit()


def reset():
    # todo: recreate board, place controller at the starting position
    raise NotImplemented


ui: Optional[UI] = None
if "--no-ui" not in sys.argv:
    ui = UI()

board_manager = BoardManager()
# controller: BaseController = LWalk()
controller: BaseController = RandomWalk()

while True:
    if ui:
        if ui.check_if_terminated():
            exit_smoothly()
        ui.draw(board=board_manager.get_current_board(), actor_path=controller.get_actor_path())

    board_manager.update_actor_position(controller.move())

    if logic.has_game_ended(controller.get_current_position()):
        print("game ended")
        logic.rate_result(actor_path=controller.get_actor_path(), starting_board=board_manager.get_starting_board())

        if ui:
            time.sleep(game_end_delay)
        reset()
    elif ui:
        time.sleep(frame_delay)
        print("tick")
