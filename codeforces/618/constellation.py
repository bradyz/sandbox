def sign(x, y, z):
    return (x[0] - z[0]) * (y[1] - z[1]) - (y[0] - z[0]) * (x[1] - z[1])


def inTriangle(pt, v1, v2, v3):
    b1 = sign(pt, v1, v2) < 0
    b2 = sign(pt, v2, v3) < 0
    b3 = sign(pt, v3, v1) < 0
    return ((b1 == b2) and (b2 == b3))


if __name__ == "__main__":
    n = int(input())
    points = [list(map(int, input().split())) + [i+1] for i in range(n)]
    points.sort()

    ret = list()

    for i in range(2, n):
        a, b, c = points[i-2], points[i-1], points[i]
        if sign(a, b, c) == 0:
            continue
        min_x = min(a[0], b[0], c[0])
        min_y = min(a[1], b[1], c[1])
        max_x = max(a[0], b[0], c[0])
        max_y = max(a[1], b[1], c[1])
        good = True
        for j in range(n):
            if points[j][0] >= max_x or points[j][0] <= min_x or \
                    points[j][1] >= max_y or points[j][1] <= min_y:
                break
            if inTriangle(points[j], a, b, c):
                good = False
                break
        for j in range(i-3, -1, -1):
            if points[j][0] >= max_x or points[j][0] <= min_x or \
                    points[j][1] >= max_y or points[j][1] <= min_y:
                break
            if inTriangle(points[j], a, b, c):
                good = False
                break
        if good:
            print(str(a[2]) + " " + str(b[2]) + " " + str(c[2]))
            break
