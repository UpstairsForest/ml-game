import time
from typing import Optional

from controllers.base_controller import BaseController
from controllers.trivial_ai import TrivialAI
from game import logic, board
from config import (
    game_end_delay, frame_delay,
)
from ui.ui import UI

# todo: replace with system arg
with_ui = True
if with_ui:
    ui: Optional[UI] = UI()
else:
    ui = None

controller: BaseController = TrivialAI()

while True:
    if ui and ui.check_if_terminated():
        exit()

    board.update_actor_position(controller.move())

    if logic.has_game_ended(controller.get_current_position()):
        print("game ended")
        if with_ui:
            time.sleep(game_end_delay)
    elif ui:
        time.sleep(frame_delay)

    if ui:
        ui.draw(board=board.get_board(), actor_path=controller.get_actor_path())
    print("tick")
