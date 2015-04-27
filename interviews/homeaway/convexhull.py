from scipy.spatial import ConvexHull
import math
import matplotlib.pyplot as plt
import numpy as np


def angle(x, y):
    res = math.atan2(float(y[1]) - float(x[1]), float(y[0]) - float(x[0]))
    return res % (2 * math.pi)


def convex_hull(arr):
    a = min(arr, key=lambda x: x[0])
    res = [a]

    b = a
    c_d = 0
    c_a = 2 * math.pi

    while len(res) == 1 or b is not a:
        for c in arr:
            if c is not b:
                d = angle(b, c)
                if d - c_d > 0 and d - c_d < c_a:
                    c_a = c_d - d
                    c_d = d
                    n_b = c
            b = n_b
            c_d = c_a
        if b is n_b:
            print(b, n_b)
            break
        b = n_b
        res.append(b)
        print("tmp: " + str(res))

    print('Res: ' + str(res))

    plt.plot(a[0], a[1], "ro")
    plt.plot([x[0] for x in res], [x[1] for x in res], "b--")

    return res


if __name__ == "__main__":
    t = np.random.rand(10, 2)
    t = [[1, 1], [0, 2], [1, 3], [2, 1], [3, 2], [2, 3]]
    n = len(t)

    hull = ConvexHull(t, 2)

    x_rim = [t[i][0] for i in hull.vertices]
    y_rim = [t[i][1] for i in hull.vertices]

    x_rim += [x_rim[0]]
    y_rim += [y_rim[0]]

    plt.plot([t[i][0] for i in range(n)], [t[i][1] for i in range(n)], 'bo')
    # plt.plot(x_rim, y_rim, "r--")

    plt.ylim([0, 4])
    plt.xlim([-1, 4])

    convex_hull(t)

    plt.show()
