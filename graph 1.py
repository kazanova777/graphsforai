import matplotlib.pyplot as plt
import numpy as np

# Variables for the sketch
actions = np.arange(0, 1000)  
game_states = np.exp(actions * 0.005)  
computational_difficulty = game_states / 100  

# Non-linear progression representing the balance between exploration and exploitation
balance_progression = 100 + 10 * np.sin(actions * 0.1) + actions * 0.1

fig, ax1 = plt.subplots(figsize=(12, 6))

# Plotting the exponential growth of game states
ax1.plot(actions, game_states, 'b-', label='Growth of Game States')
ax1.set_xlabel('Actions Made (Number of Moves)')
ax1.set_ylabel('Number of Game States', color='b')
ax1.tick_params('y', colors='b')
ax1.set_title('Complexity of Game States and Computational Difficulty in Backgammon RL')
ax1.grid(True)

# Create a twin Axes sharing the x-axis
ax2 = ax1.twinx()

ax2.plot(actions, computational_difficulty, 'r--', label='Computational Difficulty')
ax2.set_ylabel('Computational Difficulty', color='r')
ax2.tick_params('y', colors='r')

ax3 = ax1.twinx()

# Offset the twin Axes to avoid overlapping y-axes
ax3.spines['right'].set_position(('outward', 60))
ax3.plot(actions, balance_progression, 'g-.', label='Exploration-Exploitation Balance')
ax3.set_ylabel('Balance Progression', color='g')
ax3.tick_params('y', colors='g')


ax1.legend(loc='upper left')
ax2.legend(loc='upper center')
ax3.legend(loc='upper right')


plt.show()
