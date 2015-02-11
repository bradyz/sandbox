import sys
import numpy as np


def max_path(grid):
    a = grid[0][0] + _max_path(grid, 1, 0)
    b = grid[0][0] + _max_path(grid, 0, 1)
    return max(a, b)


def _max_path(grid, row, col):
    right = 0
    down = 0

    if row < rows and col < cols:
        down = grid[row][col] + _max_path(grid, row+1, col)
        right = grid[row][col] + _max_path(grid, row, col+1)

    return max(down, right)


def backwards_max(grid):
    return 0

if __name__ == "__main__":
    my_grid = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            rows = int(line.strip("\n"))
            cols = int(line.strip("\n"))
            my_g = np.zeros([rows, cols], int)
        else:
            for j, num in enumerate(line.split()):
                my_g[i-1][j] = int(num)
    print(my_g)
    max_val = max_path(my_g)
    print("Max Val: " + str(max_val))
