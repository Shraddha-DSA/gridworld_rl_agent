## GridWorld RL Agent
A simple Reinforcement Learning project where an agent learns to navigate a 4×4 grid using Q-Learning and reach a goal while avoiding obstacles.

Features

- Q-Learning from scratch

- Custom GridWorld environment

- Pygame visualization

Algorithm
Q-Learning:
  
  Q(s,a) ← Q(s,a) + α [ r + γ max Q(s',a') − Q(s,a) ]
