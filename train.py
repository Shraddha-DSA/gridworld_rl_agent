from env import GridWorld
from agent import QLearningAgent
env = GridWorld()
agent = QLearningAgent()
for episode in range(1000):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state,reward,done = env.step(action)
        agent.update(state,action,reward,next_state)
        state = next_state
print("Training completed")