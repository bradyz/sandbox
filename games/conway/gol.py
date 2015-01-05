import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

grid = None

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


def init_grid(rows, cols):
    grid = np.zeros([rows, cols], dtype=int)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = round(random.random())
            return grid


def update(data):
    return 0


if __name__ == "__main__":
    rows, cols = 30, 30
    my_grid = init_grid(rows, cols)
    print str(my_grid)
    fig, ax = plt.subplots()
    mat = ax.matshow(grid)
    ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
    plt.show()
