import math
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
    res = math.atan2(float(b[1]) - float(a[1]), float(b[0]) - float(a[0]))
    if res < 0:
        return res + 2 * PI
    else:
        return res


def convex_hull(arr):
    res = []
    a = min(arr, key=lambda x: arr[0])
    res.append(a)
    b = a
    count = 0
    cont = True
    while cont:
        min_angle = .51 * PI
        min_coor = None
        for y in arr:
            if y != b:
                tmp = angle(b, y)

                if not min_coor:
                    min_coor = b

                cond = y not in res or y == a
                if cc_diff(tmp) < cc_diff(min_angle) and cond:
                    min_angle = tmp
                    min_coor = y
        if min_coor == a:
            cont = False
            break
        count += 1
        res.append(min_coor)
        b = min_coor
    return res


if __name__ == "__main__":
    with open('convexhull-input.txt', 'r') as f:
        lines = f.readlines()
    for l in lines:
        x = []
        y = []
        coor_list = l.split()
        for coor in coor_list:
            xy = coor.split(',')
            x.append(xy[0])
            y.append(xy[1])
        inp = merge_xy(x, y)
        a = inp[0]
        print str(convex_hull(inp))

    # plt.plot(x, y, 'ro')
    # plt.show()
