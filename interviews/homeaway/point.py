import functools
import unittest


# uses lt, eq to create gte, gt, ...
@functools.total_ordering
class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def left_of(self, l):
        return True

    def __eq__(self, rhs):
        return self._x == rhs._x and self._y == rhs._y

    def __lt__(self, rhs):
        return self._x < rhs._x and self._y < rhs._y

    def __str__(self):
        return str((self._x, self._y))


class Line:

    def __init__(self, p1, p2):
        self._p1 = p1 if p1 < p2 else p2
        self._p2 = p2 if p1 < p2 else p1

    def point_given_x(self, x):
        y_diff = self._p2._y - self._p1._y
        x_diff = self._p2._x - self._p1._x
        slope = y_diff / x_diff
        return Point(x, self._p1._y + slope * x)

    def point_given_y(self, y):
        y_diff = self._p2._y - self._p1._y
        x_diff = self._p2._x - self._p1._x
        slope = y_diff / x_diff
        return Point((y - self._p1._y) / slope, y)

    def __str__(self):
        return str(self._p1) + " " + str(self._p2)


class TestPoint(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Point(1, 1), Point(1, 1))

    def test_gte(self):
        self.assertGreaterEqual(Point(1, 1), Point(0, 0))


class TestLine(unittest.TestCase):

    def test_point_given_x(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_x(2))

    def test_point_given_y(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_y(2))

    @unittest.skip("not implemented")
    def test_left_of(self):
        a = Point(0, 0)
        b = Point(1, 1)
        c = Point(0, 1)
        d = Line(a, b)
        self.assertTrue(c.left_of(d))

    @unittest.skip("not implemented")
    def test_left_of_horizontal(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
