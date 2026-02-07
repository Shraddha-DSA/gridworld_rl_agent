import numpy as np
class QLearningAgent:
    def __init__(self):
        self.q = np.zeros((4,4,4))
        self.alpha = 0.1
        self.gamma = 0.9
        self.epsilon = 0.2
    def choose_action(self,state):
        if np.random.rand()<self.epsilon:
            return np.random.randint(4)
        return np.argmax(self.q[state])
    def update(self,s,a,r,s2):
        best = np.max(self.q[s2])
        self.q[s][a]+=self.alpha*(r+self.gamma*best-self.q[s][a])