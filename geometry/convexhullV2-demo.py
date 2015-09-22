import numpy as np
import matplotlib.pyplot as plt
from convexhullV2 import convex_hull

if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle("Graham Scan Demo", fontsize=14, fontweight='bold')

    # 100 random 2d arrays
    t = np.random.rand(10, 2) * 50

    # Convex hull using Graham Scan
    t_h = convex_hull(t)

    # plot the random points with cyan dots
    plt.plot([i[0] for i in t], [i[1] for i in t], 'co')

    # plot the solution points with blue dashed lines
    plt.plot([v[0] for v in t_h], [v[1] for v in t_h], 'b--')

    # plot starting point, leftmost point with red dot
    plt.plot(t_h[0][0], t_h[0][1], 'ro')

    plt.ylim([-1, 51])
    plt.xlim([-1, 51])

    plt.show()
