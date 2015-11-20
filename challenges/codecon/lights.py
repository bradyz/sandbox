class Pt():
    def __init__(self, x, y):
        self.x = x
        self.y = y


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


def onLine(p1, p2, p):
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

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    fig = plt.figure()
    plt.ylim([-50, 51])
    plt.xlim([-50, 51])
    path = [list(map(int, input().split(","))) for _ in range(int(input()))]
    forms = [list(map(int, input().split(","))) for _ in range(int(input()))]
    lights = list()
    for i in range(len(path)):
        path[i] = Pt(path[i][0], path[i][1])
        if i > 0:
            plt.plot([path[i].x, path[i-1].x], [path[i].y, path[i-1].y], "b-")
    for m, b, xs, xf in forms:
        x1, y1 = xs, m * xs + b
        x2, y2 = xf, m * xf + b
        lights.append((Pt(x1, y1), Pt(x2, y2)))
        plt.plot([x1, x2], [y1, y2], "r-")
    res = 0
    for i in range(1, len(path)):
        p2 = path[i]
        p1 = path[i-1]
        for p3, p4 in lights:
            cross = intersection(p1, p2, p3, p4)
            if cross and onLine(p1, p2, cross) and onLine(p3, p4, cross):
                plt.plot(cross.x, cross.y, "bo")
                res += 1
    print(res)
    plt.show()
