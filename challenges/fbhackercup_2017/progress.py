from math import acos, sqrt, pi


def normalize(u):
    norm = sqrt(u[0] ** 2 + u[1] ** 2)
    return (u[0] / norm, u[1] / norm)


def dot(a, b):
    a = normalize(a)
    b = normalize(b)
    return a[0] * b[0] + a[1] * b[1]


def solve(p, x, y):
    x -= 50
    y -= 50
    degrees = acos(dot((0, 50), (x, y))) / pi * 180
    if x < 0:
        degrees = -degrees
    degrees = degrees % 360
    if x ** 2 + y ** 2 > 50 ** 2:
        return "white"
    elif degrees / 360 * 100 <= p:
        return "black"
    return "white"


for i in range(1, int(input())+1):
    print("Case #%d: %s" % (i, solve(*map(int, input().split()))))
