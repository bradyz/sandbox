from random import randrange

def union(x, y, p):
    def find(z):
        if p[z] == z:
            return z
        return find(p[z])

    p[find(x)] = find(y)


def colinear(points):
    def det(a, b, c):
        return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])
    return det(*sorted(points, key=lambda x: x[0])) == 0


def max_points(points):
    p = [i for i in range(len(points))]

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            for k in range(j+1, len(points)):
                x, y, z = points[i], points[j], points[k]
                if colinear((x, y, z)):
                    union(i, j, p)
                    union(k, j, p)
    c = dict()
    m = None

    for v in p:
        c[v] = c.get(v, 0) + 1

    for v in c:
        if not m or c[v] > c[m]:
            m = v

    return max(2, c[m])


if __name__ == "__main__":
    points = [list(sorted((randrange(10), randrange(10)))) for _ in range(10)]
    import sys
    sys.setrecursionlimit(15)
    max_points(points)
