import pygame
import time
import numpy as np
from env import GridWorld
from agent import QLearningAgent

pygame.init()

WIDTH = 400
HEIGHT = 400
ROWS = 4
COLS = 4
CELL = WIDTH // COLS

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("GridWorld RL Agent")

WHITE = (255,255,255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

env = GridWorld()
agent = QLearningAgent()

for ep in range(1000):
    state = env.reset()
    done = False
    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)
        agent.update(state, action, reward, next_state)
        state = next_state

def draw_grid(agent_pos):
    screen.fill(WHITE)

    for r in range(ROWS):
        for c in range(COLS):
            rect = pygame.Rect(c*CELL, r*CELL, CELL, CELL)
            pygame.draw.rect(screen, BLACK, rect, 1)

            if env.grid[r][c] == 'X':
                pygame.draw.rect(screen, BLACK, rect)

            if (r,c) == env.goal:
                pygame.draw.rect(screen, GREEN, rect)

            if (r,c) == agent_pos:
                pygame.draw.rect(screen, BLUE, rect)

    pygame.display.update()

state = env.reset()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    draw_grid(state)
    action = np.argmax(agent.q[state])
    state, _, done = env.step(action)

    time.sleep(0.5)

    if done:
        draw_grid(state)
        time.sleep(2)
        running = False

pygame.quit()
