from env import GridWorld
from agent import QLearningAgent
import numpy as np
env = GridWorld()
agent = QLearningAgent()
state = env.reset()
path = [state]
done = False
while not done:
    action = np.argmax(agent.q[state])
    state,_,done = env.step(action)
    path.append(state)
print("Optimal path:",path)