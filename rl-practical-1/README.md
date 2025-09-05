# summary:
# In this exercise, I try to run the CartPole-v1 environment. First, I import gymnasium and create the environment.Then, reset it to obtain the first observation. After that, I use a loop where I take random actions with env.action_space.sample() and use env.step(action) to move. I print the observation, reward, and done values. Finally, I close the environment. The pole and cart move automatically, but it is random since I did not use any agent.as in excercise 2  I check what is inside the observation space and action space. I print them using print(env.observation_space) and print(env.action_space). Observation space shows continous values like cart position, velocity, pole angle and velocity. The action space is Discrete(2) so it means only left or right. I also try env.observation_space.sample() and env.action_space.sample() to see the example values. This help me to know what the agent can see and what action it can do.

# 1.What type of space is the action space? How many actions are there?
# The action space is Discrete(2).This means there are exactly 2 possible actions:
# 0 = Push the cart to the left
# 1 = Push the cart to the right

# 2. What type of space is the observation space? (Box(4,))
# The observation space is a continuous space represented by Box(4,).
# It has 4 floating-point numbers:
# Cart position (how far left/right the cart is on the track) ,Cart velocity (speed of the cart), Pole angle (tilt of the pole, in radians).... Pole angular velocity (rate at which the pole is falling/tilting)

# 3.What does the reward represent?
# The reward is +1 for every timestep that the pole remains upright and the cart does not go out of bounds. So the longer the pole is balanced, the higher the total reward.

# 4.The final average reward you calculated for the random agent in Exercise 2. was Average reward over 1000 episodes:     0.0170
https://github.com/ChetanGhimiray/SS2025_MLA202_03240343/blob/master/rl-practical-1/Screenshot%202025-09-05%20095814.png



