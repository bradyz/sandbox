import math
import matplotlib.pyplot as plt
import numpy as np


# gives the angle between two points
def angle(x, y):
    res = math.atan2(float(y[1]) - float(x[1]), float(y[0]) - float(x[0]))
    return res % (2 * math.pi)


# Jarvis Marching Algorithm O(nh)
# n => number of points in rim
# h => number of points - 1
# TODO: add fix for vertical edges
def jarvis(arr):
    # a => leftmost point
    a = min(arr, key=lambda x: x[0])
    res = [a]

    b = a
    c_ang = 1.5 * math.pi

    # check we have not hit the starting point again
    while len(res) == 1 or not np.array_equal(b, a):
        m_diff = 2 * math.pi

        # looking for new match
        for c in arr:
            # np n-dim arrays cant check equality with keyword "is"
            if not np.array_equal(c, b):
                tmp_a = angle(b, c)
                tmp_diff = (c_ang - tmp_a) % (2 * math.pi)

                # looking for the minimum difference from previous angle
                if tmp_diff < m_diff:
                    m_diff = tmp_diff
                    new_b = c
                    tmp_c = tmp_a

        # set b to the point with minimum difference
        b = new_b
        c_ang = tmp_c

        # add to result array
        res.append(b)

    return res


# Graham Scan Algorithm O(n log n)
def graham(arr):
    return 0


def minkowski(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i+j)

    if res:
        res.append(res[0])

    return res


def minkowski_dif(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i-j)

    if res:
        res.append(res[0])

    return res


if __name__ == "__main__":
    # 100 random 2d arrays
    # t = np.random.rand(10, 2) * 50

    # array of x coordinates of solutions
    # x_rim = [t[i][0] for i in hull.vertices]
    # x_rim += [x_rim[0]]

    # array of y coordinates of solutions
    # y_rim = [t[i][1] for i in hull.vertices]
    # y_rim += [y_rim[0]]

    # jarvis algorithm using modular subtraction
    # t_h = jarvis(t)

    # plot the solution points with blue dashed lines
    # plt.plot([v[0] for v in t_h], [v[1] for v in t_h], 'b--')

    # plot starting point, leftmost point with red dot
    # plt.plot(t_h[0][0], t_h[0][1], 'ro')

    # axis
    # plt.ylim([-1, 51])
    # plt.xlim([-1, 51])

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
