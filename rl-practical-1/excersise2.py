import gymnasium as gym

# Create the FrozenLake environment
env = gym.make("FrozenLake-v1")

# Number of episodes to run
num_episodes = 1000
rewards_per_episode = []

for episode in range(num_episodes):
    # Reset environment at the start of each episode
    observation, info = env.reset()
    terminated, truncated = False, False
    episode_reward = 0

    while not terminated and not truncated:
        # Choose a random action
        action = env.action_space.sample()

        # Take the step in the environment
        next_observation, reward, terminated, truncated, info = env.step(action)

        # Add the reward
        episode_reward += reward

        # Update observation (not needed for random agent but included for clarity)
        observation = next_observation

    # Store the reward from this episode
    rewards_per_episode.append(episode_reward)

# After all episodes, compute the average reward
average_reward = sum(rewards_per_episode) / num_episodes
print(f"Average reward over {num_episodes} episodes: {average_reward:.4f}")

# Close the environment
env.close()
