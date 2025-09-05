1. What type of space is the action space? How many actions are there?
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