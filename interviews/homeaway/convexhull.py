from scipy.spatial import ConvexHull
import math
import matplotlib.pyplot as plt
import numpy as np


def angle(x, y):
    res = math.atan2(float(y[1]) - float(x[1]), float(y[0]) - float(x[0]))
    if res >= math.pi:
        res -= 2 * math.pi
    return res


def convex_hull(arr):
    a = min(arr, key=lambda x: x[0])
    res = [a]

    b = a
    c_ang = 1.5 * math.pi

    while len(res) == 1 or b is not a:
        m_diff = 2 * math.pi
        for c in arr:
            if c is not b:
                tmp_a = angle(b, c)

                if c_ang - tmp_a > 0 and c_ang - tmp_a < m_diff:
                    m_diff = c_ang - tmp_a
                    new_b = c
                    tmp_c = tmp_a

        if b is new_b:
            break

        b = new_b
        c_ang = tmp_c

        res.append(b)

    res += [res[0]]

    plt.plot(a[0], a[1], "ro")
    plt.plot([x[0] for x in res], [x[1] for x in res], "b--")

    return res


if __name__ == "__main__":
    t = np.random.rand(10, 2) * 5
    # t = [[1, 1], [0, 2], [1, 3], [2, 1], [3, 2], [2, 3], [1, 2], [2, 2]]
    n = len(t)

    hull = ConvexHull(t, 2)

    x_rim = [t[i][0] for i in hull.vertices]
    x_rim += [x_rim[0]]

    y_rim = [t[i][1] for i in hull.vertices]
    y_rim += [y_rim[0]]

    plt.plot([t[i][0] for i in range(n)], [t[i][1] for i in range(n)], 'bo')
    # plt.plot(x_rim, y_rim, "r--")

    plt.ylim([-1, 6])
    plt.xlim([-1, 6])

    convex_hull(t)

    plt.show()
