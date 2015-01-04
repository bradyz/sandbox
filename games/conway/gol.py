import numpy as np
import random
import matplotlib.pyplot as plt


def step(grid):
    print 0


def init_grid(rows, cols):
    grid = np.zeros([rows, cols], dtype=int)
    for i in range(rows):
        for j in range(cols):
            grid[i][j] = round(random.random())
            return grid


if __name__ == "__main__":
    print str(init_grid(10, 10))
    pars = 3, 2, 3
    rows, cols = 20, 20
    fig = plt.figure()
    ax = plt.axes()
    im = ax.matshow(init_grid(rows, cols), cmap=plt.cm.binary)
    im.set_data(init_grid(rows, cols))
    ax.set_axis_off()


def animate(i):
    a = im.get_array()
    a = evolve_random(a)
    im.set_array(a)
    return [im]
