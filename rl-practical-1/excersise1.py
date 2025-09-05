import gymnasium as gym
import time

# Create the CartPole environment
env = gym.make("CartPole-v1", render_mode="human")

# Print the action space and observation space
print(f"Action Space: {env.action_space}")       # Discrete(2)
print(f"Observation Space: {env.observation_space}")  # Box(4,)

# 1. What type of space is the action space? How many actions are there?
#    → The action space is Discrete(2).
#      This means there are exactly 2 possible actions:
#         0 = Push the cart to the left
#         1 = Push the cart to the right
#
# 2. What type of space is the observation space? (Box(4,))
#    → The observation space is a continuous space represented by Box(4,).
#      It has 4 floating-point numbers:
#         - Cart position (how far left/right the cart is on the track)
#         - Cart velocity (speed of the cart)
#         - Pole angle (tilt of the pole, in radians)
#         - Pole angular velocity (rate at which the pole is falling/tilting)
#
# 3. What does the reward represent?
#    → The reward is +1 for every timestep that the pole remains upright
#      and the cart does not go out of bounds. 
#      So the longer the pole is balanced, the higher the total reward.
# -----------------------------

# --- THE MAIN LOOP (RANDOM AGENT) ---
observation, info = env.reset()
terminated = False
truncated = False
total_reward = 0.0

while not terminated and not truncated:
    env.render()

    # Choose a random action (either 0 or 1)
    action = env.action_space.sample()
    print(f"Taking action: {action} (0: Left, 1: Right)")

    # Step the environment
    next_observation, reward, terminated, truncated, info = env.step(action)

    # Update episode tracking
    total_reward += reward
    observation = next_observation

    # Add a short delay for visualization
    time.sleep(0.5)

print(f"\nEpisode finished! Total Reward: {total_reward}")

# Close the environment
env.close()
