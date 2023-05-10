import sys
import time
from typing import Optional

from controllers.base_controller import BaseController

from controllers.the_abominable_0 import TheAbominable0
from game.board import BoardManager
from config import game_end_delay, step_limit, model_save_interval
from ui.progress_bar import print_progress_bar
from ui.ui import UI


def exit_smoothly():
    print("Exiting smoothly")
    global controller
    print("Saving weights")
    controller.save()
    exit()


def reset():
    global game_number
    game_number += 1

    if game_number % model_save_interval == 0:
        print(f"Saving weights on game {game_number}: ")
        controller.save()

    board_manager.reset()
    controller.reset()


ui: Optional[UI] = None
if "--no-ui" not in sys.argv:
    ui = UI()

board_manager = BoardManager()
controller: BaseController = TheAbominable0(board_manager)

game_number = 0
step = 0
while True:
    try:
        if step >= step_limit:
            print(f"failed to finish on game {game_number + 1}: ")
            reset()
            step = 0

        board_manager.update_actor_position(controller.move())
        if ui:
            ui.draw(
                board=board_manager.get_current_board(),
                actor_path=controller.get_actor_path(),
                failed_to_move=board_manager.failed_to_move(),
            )
            if ui.check_if_terminated():
                exit_smoothly()
        else:
            # only works when starting from terminal
            print_progress_bar(step, step_limit, prefix=f"game {game_number + 1}:")

        if board_manager.has_game_ended(controller.get_current_position()):
            if ui:
                time.sleep(game_end_delay)
            reset()
            step = 0
        # elif ui:
        #     time.sleep(frame_delay)

        step += 1
    except Exception as e:
        print(f"{e} on game {game_number + 1}: ")
        reset()
        step = 0

    except KeyboardInterrupt:
        exit_smoothly()
