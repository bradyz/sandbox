import sys
import numpy as np
from copy import copy


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
    new_g = copy(grid)
    for r in range(rows - 1, -1, -1):
        for c in range(cols - 1, -1, -1):
            if r == rows - 1:
                if c < cols - 1:
                    new_g[r][c] += new_g[r][c + 1]
            elif c == cols - 1:
                if r < rows - 1:
                    new_g[r][c] += new_g[r + 1][c]
            else:
                new_g[r][c] += max(new_g[r + 1][c], new_g[r][c + 1])

    print(new_g)
    return new_g[0][0]

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            rows = int(line.strip("\n"))
            cols = int(line.strip("\n"))
            my_g = np.zeros([rows, cols], int)
        else:
            for j, num in enumerate(line.split()):
                my_g[i-1][j] = int(num)
    print("Start Grid: ")
    print(str(my_g))
    max_val = max_path(my_g)
    print("O(2^nm): " + str(max_val) + "\n")
    print("Backwards Grid: ")
    second_val = backwards_max(my_g)
    print("O(nm): " + str(second_val))

# Given a 2d grid of integers, find the max sum of the path
# starting from the top left going to the bottom right
# assuming that you can only move to the right (col + 1)
# and down (row + 1)
