# from matplotlib import pyplot as plt
from sys import maxsize as INT_MAX


class Pt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, b):
        return self.x == b.x and self.y == b.y

    def __str__(self):
        return str(self.x) + " " + str(self.y)


def intersection(p1, p2, p3, p4):
    d = (p4.y - p3.y)*(p2.x-p1.x) - (p4.x - p3.x)*(p2.y - p1.y)
    if d == 0:
        return None
    ua = (p4.x - p3.x)*(p1.y-p3.y) - (p4.y-p3.y)*(p1.x-p3.x)
    ua /= d
    ub = (p2.x - p1.x)*(p1.y-p3.y) - (p2.y-p1.y)*(p1.x-p3.x)
    ub /= d
    r = Pt(p2.x-p1.x, p2.y-p1.y)
    r.x *= ua
    r.y *= ua
    return Pt(r.x+p1.x, r.y+p1.y)


def on(p1, p2, p):
    def trap(a, b):
        return (0.5*(b.x - a.x)*(b.y + a.y))

    def triarea(a, b, c):
        return abs(trap(a, b)+trap(b, c)+trap(c, a))
    s = triarea(p, p1, p2)
    if s > 0:
        return False
    sg = (p.x-p1.x)*(p.x-p2.x)
    if sg > 0:
        return False
    sg = (p.y-p1.y)*(p.y-p2.y)
    if sg > 0:
        return False
    return True

coor = [list(map(int, input().split())) for _ in range(3)]

ret = INT_MAX

for i, j, k in ([0, 1, 2], [0, 2, 1], [1, 0, 2]):
    tmp = 0
    first = list()
    second = list()
    a = Pt(*coor[i])
    b = Pt(*coor[j])
    c = Pt(*coor[k])
    if a.x == b.x or a.y == b.y:
        first.append([(a, b)])
    else:
        first.append([(a, Pt(a.x, b.y)), (Pt(a.x, b.y), b)])
        first.append([(a, Pt(b.x, a.y)), (Pt(b.x, a.y), b)])
    if b.x == c.x or b.y == c.y:
        for path in first:
            second.append(path + [(b, c)])
    else:
        for path in first:
            second.append(path + [(b, Pt(b.x, c.y)), (Pt(b.x, c.y), c)])
            second.append(path + [(b, Pt(c.x, b.y)), (Pt(c.x, b.y), c)])
    for path in second:
        good = True
        path_len = len(path)
        for i in range(len(path)):
            if not good:
                break
            for j in range(i+1, len(path)):
                a, b = path[i]
                c, d = path[j]
                x = intersection(a, b, c, d)
                if x and on(a, b, x) and on(c, d, x) and [a, b, c, d].count(x) == 1:
                    good = False
                    break
                if (on(a, b, c) and on(a, b, d)) or (on(c, d, a) and on(c, d, b)):
                    good = False
                    break
                if x and [a, b, c, d].count(x) == 1 and (on(a, b, c) or on(a, b, d) or on(c, d, a) or on(c, d, b)):
                    # plt.plot(a.x, a.y, "bo")
                    # plt.plot(b.x, b.y, "bo")
                    # plt.plot(c.x, c.y, "bo")
                    # plt.plot(d.x, d.y, "bo")
                    # plt.plot([a.x, b.x], [a.y, b.y], "g-")
                    # plt.plot([c.x, d.x], [c.y, d.y], "g-")
                    # plt.plot(x.x, x.y, "ro")
                    # plt.show()
                    good = False
                    break
                if not x and ((c == b) or (a == c) or (a == d)):
                    path_len -= 1
        if good and path_len < ret:
            # for i in range(len(path)):
            #     x = path[i][0]
            #     y = path[i][1]
            #     plt.plot(x.x, x.y, "ro")
            #     plt.plot(y.x, y.y, "ro")
            #     plt.plot([x.x, y.x], [x.y, y.y], "b-")
            #     x = path[i-1][0]
            #     y = path[i-1][1]
            #     plt.plot(x.x, x.y, "ro")
            #     plt.plot(y.x, y.y, "ro")
            #     plt.plot([x.x, y.x], [x.y, y.y], "r-")
            #     plt.show()
            ret = path_len
# plt.plot([x[0] for x in coor], [y[1] for y in coor], "ro")
# plt.show()
print(ret)
