import gym
import tensorflow as tf
import numpy as np
from PIL import Image

from model import ActorCritic


def render_episode(env: gym.Env, model: tf.keras.Model, max_steps: int):
    state, info = env.reset()
    state = tf.constant(state, dtype=tf.float32)
    screen = env.render()
    images = [Image.fromarray(screen)]

    for i in range(1, max_steps + 1):
        # state = tf.expand_dims(state, 0)
        state = tf.convert_to_tensor(state)
        action_probs, _ = model(state)
        action = np.argmax(np.squeeze(action_probs))

        state, reward, done, truncated, info = env.step(action)
        state = tf.constant(state, dtype=tf.float32)

        # Render screen every step
        screen = env.render()
        images.append(Image.fromarray(screen))

        if done:
            break

    return images


max_steps_per_episode = 500

model = ActorCritic(4, 128)
model.load_weights("./checkpoints/model_weights")

# Visualization
# Render an episode and save as a GIF file

render_env = gym.make("gym_stuff:Environment-v0", render_mode="rgb_array")

# Save GIF image
images = render_episode(render_env, model, max_steps_per_episode)
image_file = "cartpole-v1.gif"
# loop=0: loop forever, duration=1: play each frame for 1ms
images[0].save(image_file, save_all=True, append_images=images[1:], loop=0, duration=1)
