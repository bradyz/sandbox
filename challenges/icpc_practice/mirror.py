# from matplotlib import pyplot as plt
from math import sqrt


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def norm(x):
    n = sqrt(x[0] ** 2 + x[1] ** 2)
    return (x[0] / n, x[1] / n)


def dot(x, y):
    return x[0] * y[0] + x[1] * y[1]


def reflect(x, y, dx, dy, n, px, py):
    rx = x - px
    ry = y - py
    r = norm((rx, ry))

    if dot(r, n) < 0:
        n = (-n[0], -n[1])

    d = dot(r, n)

    nx = 2 * n[0] * d - r[0]
    ny = 2 * n[1] * d - r[1]

    return (px + 1e-7 * nx, py + 1e-7 * ny, nx, ny)


def intersect(x, y, dx, dy, x1, y1, x2, y2):
    a = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1)
    b = dy * (x2 - x1) - dx * (y2 - y1)

    if abs(b) < 1e-7:
        return None

    t = -a / b

    if t < 1e-7:
        return None

    px, py = x + dx * t, y + dy * t

    d1 = sqrt((px - x1) ** 2 + (py - y1) ** 2)
    d2 = sqrt((px - x2) ** 2 + (py - y2) ** 2)
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    if d1 > d or d2 > d:
        return None

    return (px + dx * 1e-7, py + dy * 1e-7)


def solve(x, y, dx, dy, detectors, splitters, mirrors):
    s = [(x, y, dx, dy)]
    hit = [False for _ in range(len(detectors))]

    while s:
        x, y, dx, dy = s.pop()
        dx, dy = norm((dx, dy))

        closest = (int(1e9), int(1e9))
        closest_type = None
        closest_normal = None

        # plt.plot([x, x+dx*5], [y, y+dy*5], "b--")
        # plt.plot(x, y, "bo")

        for i, detector in enumerate(detectors):
            # plt.plot([detector[0], detector[2]],[detector[1], detector[3]],"g-")
            isect = intersect(x, y, dx, dy, *detector)
            if isect and dist(x, y, *isect) < dist(x, y, *closest):
                closest_type = "D"
                closest = isect
                closest_normal = i

        for i, splitter in enumerate(splitters):
            # plt.plot([splitter[0], splitter[2]],[splitter[1], splitter[3]],"c-")
            isect = intersect(x, y, dx, dy, *splitter)
            if isect and dist(x, y, *isect) < dist(x, y, *closest):
                x1, y1, x2, y2 = splitter
                closest_type = "S"
                closest = isect
                closest_normal = norm((1, -(x2 - x1) / (y2 - y1)))

        for i, mirror in enumerate(mirrors):
            # plt.plot([mirror[0], mirror[2]],[mirror[1], mirror[3]],"r-")
            isect = intersect(x, y, dx, dy, *mirror)
            x1, y1, x2, y2 = mirror
            if isect and dist(x, y, *isect) < dist(x, y, *closest):
                x1, y1, x2, y2 = mirror
                closest_type = "M"
                closest = isect
                closest_normal = norm((1, -(x2 - x1) / (y2 - y1)))

        if not closest_type:
            continue
        elif closest_type == "D":
            # plt.plot(closest[0], closest[1], "ro")
            hit[closest_normal] = True
        elif closest_type == "M":
            s.append(reflect(x, y, dx, dy, closest_normal, *closest))
        else:
            s.append(reflect(x, y, dx, dy, closest_normal, *closest))
            s.append((closest[0], closest[1], dx, dy))

    return hit


for test in range(int(input())):
    a, b = input().split()
    x, y = map(int, a.split(","))
    dx, dy = map(int, b.split(","))
    detectors = list()
    splitters = list()
    mirrors = list()
    num = list()
    for i in range(int(input())):
        o, p1, p2 = input().split()
        p1, p2 = list(map(int, p1.split(","))), list(map(int, p2.split(",")))
        if o == "M":
            mirrors.append((p1[0], p1[1], p2[0], p2[1]))
        elif o == "S":
            splitters.append((p1[0], p1[1], p2[0], p2[1]))
        else:
            detectors.append((p1[0], p1[1], p2[0], p2[1]))
            num.append(i+1)
    hit = solve(x, y, dx, dy, detectors, splitters, mirrors)
    print("DATA SET #%d" % (test+1))
    can = False
    for i in range(len(hit)):
        if hit[i]:
            can = True
            print(num[i])
    if not can:
        print("NO BEAMS DETECTED")
    # plt.xlim(0, 100)
    # plt.ylim(0, 100)
    # plt.show()
