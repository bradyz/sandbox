from math import acos, pi
from convexhullV2 import det


# assumes a and b are vectors in 2D
def magnitude(v):
    return abs(v[0] ** 2 + v[1]**2)


def dot(a, b):
    return a[0]*b[0] + a[1]*b[1]


# when two points are equal the magnitude will be 0
def angle(a, b, c):
    ba = (a[0]-b[0], a[1]-b[1])
    bc = (c[0]-b[0], c[1]-b[1])
    if det(a, b, c) > 0:
        sign = 1
    else:
        sign = -1
    return sign * acos(dot(ba, bc) / magnitude(ba) / magnitude(bc)) % (2 * pi)


# a is left of b
def is_left(a, b):
    return a[0] < b[0]


def is_right(a, b):
    return a[0] > b[0]


# b is below a
def is_below(b, a):
    return a[1] >= b[1] and (is_left(a, b) ^ is_right(a, b))


def is_start_vertex(a, b, c):
    return angle(a, b, c) < pi and is_below(a, b) and is_below(a, c)


def is_split_vertex(a, b, c):
    return angle(a, b, c) > pi and is_below(a, b) and is_below(a, c)


if __name__ == "__main__":
    print(angle((0, 0), (1, 1), (2, 0)))
    print(angle((2, 0), (1, 1), (0, 0)))
