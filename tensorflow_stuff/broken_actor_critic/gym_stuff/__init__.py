from gym.envs.registration import register

register(
    id="Environment-v0",
    entry_point="gym_stuff.adapter:Environment",
    max_episode_steps=300,
)
