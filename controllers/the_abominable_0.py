import os.path
from dataclasses import replace
from typing import List, Optional

import numpy as np
import tensorflow as tf

from config import board_width
from controllers.lwalk import LWalk
from game import logic
from game.board import BoardManager
from models.game_models import Move, Position, Square


class TheAbominable0(LWalk):
    """Basically tries to recreate the reward system of the game"""

    board_manager: BoardManager

    _model: tf.keras.Model
    _checkpoint_path = os.path.join(
        os.getcwd(), f"fixtures/checkpoints/the_abominable_0_bw{board_width}/cp.ckpt"
    )

    def __init__(self, board_manager: BoardManager):
        # it's 'abominable' for a reason
        self.board_manager = board_manager
        super().__init__()

        # layers
        # The model is compiled complete from start
        # rather than extended with Softmax on each move to avoid retracing, potentially
        # at least tf complains less
        self._model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dense(4),  # the number of possible moves
                tf.keras.layers.Softmax(),
            ]
        )
        # compile
        self._model.compile(
            loss=tf.keras.losses.SparseCategoricalCrossentropy(),
            optimizer="adam",
            metrics=["accuracy"],
        )
        # get data if exists
        try:
            self._model.load_weights(
                tf.train.latest_checkpoint(os.path.dirname(self._checkpoint_path))
            )
        except Exception as e:
            print(f"Failed to load weights:\n{e}")

    def move(self) -> Optional[Move]:
        # get training data for current state:
        # n*n flattened board
        flat_board = []
        for row in self.board_manager.get_current_board():
            for square in row:
                flat_board.append(self._square_to_numeric(square))
        # 4 possible moves with scores
        moves: List[Move] = [
            Move(
                start=self.current_position,
                end=Position(x=self.current_position.x - 1, y=self.current_position.y),
            ),
            Move(
                start=self.current_position,
                end=Position(x=self.current_position.x + 1, y=self.current_position.y),
            ),
            Move(
                start=self.current_position,
                end=Position(x=self.current_position.x, y=self.current_position.y + 1),
            ),
            Move(
                start=self.current_position,
                end=Position(x=self.current_position.x, y=self.current_position.y - 1),
            ),
        ]
        current_board = self.board_manager.get_current_board()
        # rate and scale
        move_scores = (
            np.asarray([logic.rate_move(move, current_board) for move in moves]) * 100
        )

        best_move_index = np.argmax(move_scores)

        data = tf.convert_to_tensor(
            np.expand_dims(np.asarray(flat_board, dtype=np.float32), 0)
        )
        goal = tf.convert_to_tensor(np.expand_dims(best_move_index, 0))

        # fit
        self._model.fit(data, goal, epochs=3, verbose=0)
        # predict
        prediction = self._model.predict(data, verbose=0)
        predicted_move: Move = moves[np.argmax(prediction)]

        # update controller-related fields
        if not logic.is_move_valid(predicted_move):
            return None
        self.current_position = predicted_move.end
        self.actor_path.append(self.current_position)
        return predicted_move

    def reset(self):
        self.current_position = replace(logic.get_actor_starting_position())
        self.actor_path = []

    @staticmethod
    def _square_to_numeric(square: Square) -> int:
        # values are arbitrary
        square_map = {
            Square.EMPTY: 0,
            Square.START: 2,
            Square.ACTOR: 1,
            Square.END: -1,
            Square.COIN: -2,
        }
        return square_map[square]

    def save(self):
        self._model.save_weights(self._checkpoint_path)
