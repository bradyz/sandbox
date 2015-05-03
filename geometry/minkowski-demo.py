import numpy as np
import matplotlib.pyplot as plt
from convexhull import jarvis, minkowski_dif


if __name__ == "__main__":
    # two triangles
    t = np.random.rand(3, 2) * 5
    t = np.concatenate((t, [t[0]]), axis=0)

    t1 = np.random.rand(3, 2) * 5
    t1 = np.concatenate((t1, [t1[0]]), axis=0)

    # t = np.array([[0, 1],
    #               [0, -1],
    #               [1, 0],
    #               [0, 1]])
    #
    # t1 = np.array([[1, 1],
    #                [1, -1],
    #                [0, 0],
    #                [1, 1]])

    n = len(t)

    # minkowski test axis
    plt.ylim([-10, 10])
    plt.xlim([-10, 10])

    # plot all of the points with cyan dot
    plt.plot([t[i][0] for i in range(n)], [t[i][1] for i in range(n)], 'r-')
    plt.plot([t1[i][0] for i in range(n)], [t1[i][1] for i in range(n)], 'b-')

    # convex hull of minkowski addition of t and t1
    ms = jarvis(minkowski_dif(t, t1))
    m = len(ms)

    # plot minkowski convex hull
    plt.plot([ms[i][0] for i in range(m)], [ms[i][1] for i in range(m)], 'c--')

    plt.plot([0], [0], "ko")

    # show plot
    plt.show()
