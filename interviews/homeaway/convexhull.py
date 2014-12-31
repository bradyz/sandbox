import math as math
# import matplotlib.pyplot as plt


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


def convex_hull(arr):
    a = min(arr, key=lambda x: arr[0])
    print math.atan2(float(a[1]), float(a[0]))


if __name__ == "__main__":
    with open('testplot-input.txt', 'r') as f:
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
        convex_hull(inp)

    # plt.plot(x, y, 'ro')
    # plt.show()
