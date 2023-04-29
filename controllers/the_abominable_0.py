import os.path
from typing import List

import numpy as np
import tensorflow as tf

from controllers.lwalk import LWalk
from game import logic
from game.board import BoardManager
from models.game_models import Move, Position, Square


class TheAbominable0(LWalk):
    """Basically tries to recreate the reward system of the game"""

    model: tf.keras.Model
    board_manager: BoardManager
    print(os.getcwd())
    checkpoint_path = os.path.join(
        os.getcwd(), "fixtures/checkpoints/the_abominable_0/cp.ckpt"
    )
    print(checkpoint_path)

    def __init__(self, board_manager: BoardManager):
        # it's 'abominable' for a reason
        self.board_manager = board_manager
        super().__init__()

        # layers
        self.model = tf.keras.Sequential(
            [
                tf.keras.layers.Dense(128, activation="relu"),
                tf.keras.layers.Dense(4),  # the number of possible moves
            ]
        )
        # compile
        self.model.compile(
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            optimizer="adam",
            metrics=["accuracy"],
        )
        # get data if exists
        try:
            self.model.load_weights(
                tf.train.latest_checkpoint(os.path.dirname(self.checkpoint_path))
            )
        except Exception as e:
            print(f"Failed to load weights:\n{e}")

    def move(self) -> Move:
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
        move_scores = [
            logic.rate_move(move, self.board_manager.get_current_board())
            for move in moves
        ]
        best_move_index = np.argmax(move_scores)

        data = np.expand_dims(np.asarray(flat_board, dtype=np.float32), 0)
        goal = np.expand_dims(best_move_index, 0)
        cp_callback = tf.keras.callbacks.ModelCheckpoint(
            filepath=self.checkpoint_path,
            verbose=1,
            save_weights_only=True,
        )

        # fit
        self.model.fit(data, goal, epochs=3, verbose=0, callbacks=[cp_callback])
        # predict
        prediction_model = tf.keras.Sequential([self.model, tf.keras.layers.Softmax()])
        prediction = prediction_model.predict(data, verbose=0)
        predicted_move: Move = moves[np.argmax(prediction)]

        # update controller-related fields
        self.current_position = predicted_move.end
        self.actor_path.append(self.current_position)
        return predicted_move

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
