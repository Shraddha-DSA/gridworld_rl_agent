import numpy as np
class GridWorld:
    def __init__(self):
        self.size = 4
        self.grid = np.array([
            ['S','.','.','.'],
            ['X','X','.','.'],
            ['.','.','.','X'],
            ['.','.','.','G']
        ])
        self.start = (0,0)
        self.goal = (3,3)
        self.state = self.start
    
    def reset(self):
        self.state = self.start
        return self.state
    def step(self,action):
        row,col = self.state
        if action==0: row -=1
        if action==1: row+=1
        if action==2: col-=1
        if action==3: col+=1

        if row<0 or row>=4 or col<0 or col>=4:
            return self.state,-1,False
        if self.grid[row][col]=='X':
            return self.state,-10,True
        if (row,col)==self.goal:
            return (row,col),10,True
        self.state = (row,col)
        return self.state,-1,False