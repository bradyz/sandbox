from scipy.spatial import ConvexHull
import math
import matplotlib.pyplot as plt
from random import randrange

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
    res = []
    a = min(arr, key=lambda x: x[0])
    print 'Start: ' + str(a)
    res.append(a)
    b = a
    count = 0
    # cont = True
    while count == 0 or b != a:
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
        # if min_coor == a:
        #     cont = False
        #     break
        count += 1
        res.append(min_coor)
        b = min_coor
    return res


if __name__ == "__main__":
    # with open('convexhull-input.txt', 'r') as f:
    #     lines = f.readlines()
    num_points = 10

    tmp_x = [randrange(5) for i in range(10)]
    tmp_y = [randrange(5) for i in range(10)]

    given = [1]

    # for l in lines:

    for l in given:
        x = tmp_x
        y = tmp_y

        # x = []
        # y = []
        # coor_list = l.split()
        #
        # for coor in coor_list:
        #     xy = coor.split(',')
        #     x.append(xy[0])
        #     y.append(xy[1])

        inp = merge_xy(x, y)
        points = inp
        rim = convex_hull(inp)
        hull = ConvexHull(inp)
        rim_x = []
        rim_y = []

        print 'Input: ' + str(inp)
        print 'Rim: ' + str(rim)

        for i in range(len(rim)):
            tmp_coor = rim[i]
            rim_x.append(tmp_coor[0])
            rim_y.append(tmp_coor[1])

    plt.plot(x, y, 'bo')
    plt.plot(rim_x, rim_y, 'g-')
    plt.show()
