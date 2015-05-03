import math
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
