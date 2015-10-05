import numpy as np
import matplotlib.pyplot as plt
from convexhull import jarvis, minkowski_dif


if __name__ == "__main__":
    # two triangles
    t = np.random.rand(3, 2) * 5
    t = np.concatenate((t, [t[0]]), axis=0)

    t1 = np.random.rand(3, 2) * 5
    t1 = np.concatenate((t1, [t1[0]]), axis=0)

    n = len(t)

    # minkowski test axis
    plt.ylim([-5, 5])
    plt.xlim([-5, 5])

    # plot all of the points with cyan dot
    plt.plot([t[i][0] for i in range(n)], [t[i][1] for i in range(n)], 'r-')
    plt.plot([t1[i][0] for i in range(n)], [t1[i][1] for i in range(n)], 'b-')

    # convex hull of minkowski addition of t and t1
    md = minkowski_dif(t, t1)
    ms = jarvis(md)
    msl = len(ms)
    mdl = len(md)

    # plot minkowski convex hull
    plt.plot([ms[i][0] for i in range(msl)], [ms[i][1] for i in range(msl)], 'c--')

    # plot minkowski
    plt.plot([md[i][0] for i in range(mdl)], [md[i][1] for i in range(mdl)], 'co')

    plt.plot([0], [0], "ko")

    # show plot
    plt.show()
