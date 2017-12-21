from math import sqrt


class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dot(self, rhs):
        return self.x * rhs.x + self.y * rhs.y

    def cross(self, rhs):
        return self.x * rhs.y - self.y * rhs.x

    def norm_sq(self):
        return self.dot(self)

    def norm(self):
        return sqrt(self.norm_sq())

    def __add__(self, rhs):
        return Vector(self.x + rhs.x, self.y + rhs.y)

    def __sub__(self, rhs):
        return Vector(self.x - rhs.x, self.y - rhs.y)

    def __mul__(self, rhs):
        return Vector(self.x * rhs, self.y * rhs)

    def __str__(self):
        return "%s, %s" % (self.x, self.y)


def point_to_line(p1, p2, x, clamp=False):
    t = (x - p1).dot(p2 - p1) / (p2 - p1).norm_sq()

    if clamp:
        if t < 0.0:
            return p1
        elif t > 1.0:
            return p2

    return p1 + (p2 - p1) * t
