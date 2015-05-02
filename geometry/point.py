import matplotlib.pyplot as plt
import functools


# uses lt, eq to create gte, gt, ...
@functools.total_ordering
class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def left_of(self, l):
        a = l.point_given_y(self._y)
        if a:
            return self._x <= a._x
        else:
            return self._y >= l._p1._y

    def __eq__(self, rhs):
        return self._x == rhs._x and self._y == rhs._y

    def __lt__(self, rhs):
        return self._x < rhs._x and self._y < rhs._y

    def __str__(self):
        return str((self._x, self._y))


class Line:

    def __init__(self, p1, p2):
        if p1 == p2:
            raise ValueError("P1 must be different than P2")

        self._p1 = p1 if p1 < p2 else p2
        self._p2 = p2 if p1 < p2 else p1

        self._y_diff = self._p2._y - self._p1._y
        self._x_diff = self._p2._x - self._p1._x

        self._hor = self._y_diff == 0
        self._vrt = self._x_diff == 0

        if not self._hor and not self._vrt:
            self._slope = (p2._y-p1._y)/(p2._x-p1._x)
        else:
            self._slope = 0

    def point_given_x(self, x):
        if not self._hor and not self._vrt:
            return Point(x, self._p1._y + self._slope * (x-self._p1._x))
        else:
            return None

    def point_given_y(self, y):
        if not self._hor and not self._vrt:
            return Point(self._p1._x + (y - self._p1._y) / self._slope, y)
        else:
            return None

    def __str__(self):
        return str(self._p1) + " " + str(self._p2)


if __name__ == "__main__":
    a = Point(1, 1)
    b = Point(4, 1)
    c = Line(a, b)
    e = Point(1, 1)
    f = Point(1, 2)

    print(a)
    print(b)

    plt.ylim([-1, 10])
    plt.xlim([-1, 10])

    plt.plot([a._x, b._x], [a._y, b._y], "b--")

    plt.plot(f._x, f._y, "go")
    plt.plot(e._x, e._y, "go")

    print("F: " + str(f.left_of(c)))
    print("E: " + str(e.left_of(c)))

    plt.show()
