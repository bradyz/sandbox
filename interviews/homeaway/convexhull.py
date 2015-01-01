import math as math
# import matplotlib.pyplot as plt

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
    # res = math.atan2(b[1] - a[1], b[0] - a[1])
    res = math.atan2(float(b[1]) - float(a[1]), float(b[0]) - float(a[1]))
    if res < 0:
        return res + 2 * PI
    else:
        return res


def convex_hull(arr):
    res = []
    a = min(arr, key=lambda x: arr[0])
    res.append(a)
    b = []
    while b != a:
        min_angle = None
        for y in arr:
            tmp_angle = angle(y, x)
            if not min_angle:
                min_angle = y
            elif cc_diff(tmp_angle) < cc_diff(min_angle):
                min_angle = tmp_angle
                b = y
                print y
        res.append(b)
    return res


if __name__ == "__main__":
    with open('convexhull-input.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        x = []
        y = []
        a = l.split()
        for coor in a:
            xy = coor.split(',')
            x.append(xy[0])
            y.append(xy[1])
        inp = merge_xy(x, y)
        print str(convex_hull(inp))

    # plt.plot(x, y, 'ro')
    # plt.show()
