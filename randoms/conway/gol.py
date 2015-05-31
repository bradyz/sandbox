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
    global count
    print("Generation " + str(count))
    count += 1
    grid_copy = my_grid.copy()
    for i in range(rows):
        for j in range(cols):
            neighbors = num_neighbors(grid_copy, i, j)
            if grid_copy[i][j] == 1:
                if neighbors < 2 or neighbors > 3:
                    my_grid[i][j] = 0
            else:
                if neighbors == 3:
                    my_grid[i][j] = 1
    mat.set_data(my_grid)


def num_neighbors(grid, x_coor, y_coor):
    global rows, cols
    neighbors = 0
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x_coor + x < rows) and (x_coor + x > 0) and (y_coor + y < cols) and (y_coor + y > 0):
                neighbors += grid[x_coor + x][y_coor + y]
    return neighbors - grid[x_coor][y_coor]


if __name__ == "__main__":
    print("Conways Game of Life")
    rows, cols = 100, 100
    fig, ax = plt.subplots()
    init()
    mat = ax.matshow(my_grid)
    anim = animation.FuncAnimation(fig, animate, interval=10)
    plt.show()
