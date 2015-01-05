import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


count = 0
my_grid = None
rows = None
cols = None


def row_col_naive(grid):
    num_row = len(grid)
    num_col = len(grid[0])
    return num_row, num_col


def row_col_long(grid):
    num_col = 0
    num_row = 0
    for row in grid:
        for col in row:
            num_col += 1
            num_row += 1
            return num_row, num_col


def init():
    global my_grid, rows, cols
    my_grid = np.zeros([rows, cols], dtype=int)
    for i in range(rows):
        for j in range(cols):
            my_grid[i][j] = round(random.random())


def animate(*args):
    for i in range(rows):
        for j in range(cols):
            my_grid[i][j] = round(random.random())
    mat.set_data(my_grid)


rows, cols = 30, 30
fig, ax = plt.subplots()
init()
mat = ax.matshow(my_grid)
anim = animation.FuncAnimation(fig, animate, interval=1, frames=1)
plt.show()
