from random import randint
from matplotlib import pyplot as plt
from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __rmul__(self, x):
        return Point(self.x * x, self.y * x)

    def normalize(self):
        n = self.norm()
        self.x /= n
        self.y /= n

    def norm(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def invert(self):
        self.x, self.y = -self.y, self.x


def closest(p1, p2, p3):
    # v vector from p1 to p2.
    v = p1 - p2
    v.normalize()

    # u orthogonal to v.
    u = p2 - p1
    u.invert()
    u.normalize()

    # (p2 - p1) x (r - p1) = 0
    # (v) x (p3 + ut - p1) = 0
    # v_x * (p3_y + u_y * t - p1_y) = v_y * (p3_x + u_x * t - p1_x)
    # v_x * (p3_y - p1_y) + v_x * u_y * t = v_y * (p3_x - p1_x) + v_y * u_x * t
    # v_x * (p3_y - p1_y) - v_y * (p3_x - p1_x) = v_y * u_x * t - v_x * u_y * t
    # v_x * (p3_y - p1_y) - v_y * (p3_x - p1_x) = (v_y * u_x - v_x * u_y) * t
    # (v_x * (p3_y - p1_y) - v_y * (p3_x - p1_x)) / (v_y * u_x - v_x * u_y) = t
    t = (v.x * (p3.y - p1.y) - v.y * (p3.x - p1.x)) / (v.y * u.x - v.x * u.y)
    return p3 + t * u


if __name__ == "__main__":
    # helper.
    rand = lambda: randint(-10, 10)

    p1 = Point(rand(), rand())
    p2 = Point(rand(), rand())

    # make p1, p2 touch boundaries.
    v = p2 - p1
    v.normalize()
    t1 = (-10 - p1.x) / v.x
    t2 = (-10 - p1.y) / v.y
    if abs(t1) > abs(t2):
        p1 = p1 + t1 * v
    else:
        p1 = p1 + t2 * v
    t1 = (10 - p1.x) / v.x
    t2 = (10 - p1.y) / v.y
    if abs(t1) > abs(t2):
        p2 = p2 + t1 * v
    else:
        p2 = p2 + t2 * v

    p3 = Point(rand(), rand())
    p4 = closest(p1, p2, p3)

    # the dot of the two vectors should be 0.
    u = p3 - p4
    v = p2 - p1
    print(u.x * v.x + u.y * v.y)

    plt.xlim(-10, 10)
    plt.ylim(-10, 10)

    plt.axes().set_aspect('equal')

    plt.plot([p1.x, p2.x], [p1.y, p2.y], "b-")
    plt.plot(p3.x, p3.y, "ro")
    plt.plot(p4.x, p4.y, "ro")
    plt.show()
