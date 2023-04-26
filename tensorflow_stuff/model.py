import tensorflow as tf
from typing import Tuple


class ActorCritic(tf.keras.Model):
    """Combined actor-critic network."""

    def __init__(self, num_actions: int, num_hidden_units: int):
        """Initialize."""
        super().__init__()

        self.common = tf.keras.layers.Dense(num_hidden_units, activation="relu")
        self.actor = tf.keras.layers.Dense(num_actions)
        self.critic = tf.keras.layers.Dense(1)

    def call(
            self, inputs: tf.Tensor, training=None, mask=None
    ) -> Tuple[tf.Tensor, tf.Tensor]:
        x = self.common(inputs)
        return self.actor(x), self.critic(x)
