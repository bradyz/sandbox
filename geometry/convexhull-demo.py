import numpy as np
import matplotlib.pyplot as plt
from convexhull import jarvis

if __name__ == "__main__":
    # 100 random 2d arrays
    t = np.random.rand(20, 2) * 50

    # jarvis algorithm using modular subtraction
    t_h = jarvis(t)

    plt.plot([i[0] for i in t], [i[1] for i in t], 'co')

    # plot the solution points with blue dashed lines
    plt.plot([v[0] for v in t_h], [v[1] for v in t_h], 'b--')

    # plot starting point, leftmost point with red dot
    plt.plot(t_h[0][0], t_h[0][1], 'ro')

    # axis
    plt.ylim([-1, 51])
    plt.xlim([-1, 51])

    plt.show()
