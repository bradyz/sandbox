from scipy.spatial import ConvexHull
import math
import matplotlib.pyplot as plt
import numpy as np

PI = math.pi


def cc_diff(a, b=.5*PI):
    if a >= 0 and a <= b:
        return b - a
    else:
        return 2 * PI + b - a


def angle_pos(x):
    if x < 0:
        return 360 + x
    else:
        return x


def merge_xy(x, y):
    coor = []
    if len(x) != len(y):
        return []
    for i in range(len(x)):
        tmp = []
        tmp.append(x[i])
        tmp.append(y[i])
        coor.append(tmp)
    return coor


def rad_to_deg(r):
    return r * 180 / math.pi


def angle(a, b):
    res = math.atan2(float(b[1]) - float(a[1]), float(b[0]) - float(a[0]))
    if res < 0:
        return res + 2 * PI
    else:
        return res


def convex_hull(arr):
    a = min(arr, key=lambda x: x[0])
    res = []
    b = a
    print('Start: ' + str(a))
    count = 0
    while not res or b != a:
        min_angle = .51 * PI
        min_coor = None
        max_angle = .49 * PI
        max_coor = None
        for y in arr:
            if y != b:
                tmp = angle(b, y)

                if not min_coor:
                    min_coor = b
                if not max_coor:
                    max_coor = b

                cond = y not in res or y == a
                if cc_diff(tmp) < cc_diff(min_angle) and cond:
                    min_angle = tmp
                    min_coor = y
                if cc_diff(tmp) > cc_diff(max_angle) and cond:
                    max_angle = tmp
                    max_coor = y
        count -= 1
        res.append((b, min_coor))
        b = min_coor
    return res


if __name__ == "__main__":
    num_points = 10

    test = np.random.rand(10, 2)

    points = test
    print(test)
    hull = ConvexHull(test, 2)

    print(test[hull.vertices, 0])

    plt.plot(test[:, 0], test[:, 1], 'bo')
    plt.plot(test[hull.vertices, 0], test[hull.vertices, 1], "r--")
    plt.plot(test[hull.vertices[0], 0], test[hull.vertices[0], 1], 'ro')

    plt.show()
