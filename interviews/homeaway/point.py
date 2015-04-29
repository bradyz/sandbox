import functools
import unittest


# uses lt, eq to create gte, gt, ...
@functools.total_ordering
class Point:

    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __eq__(self, rhs):
        return self._x == rhs._x and self._y == rhs._y

    def __lt__(self, rhs):
        return self._x < rhs._x and self._y < rhs._y

    def __str__(self):
        return str((self._x, self._y))


class Line:

    def __init__(self, p1=Point(), p2=Point()):
        self._p1 = p1 if p1 < p2 else p2
        self._p2 = p2 if p1 < p2 else p1

    def __str__(self):
        return str(self._p1) + " " + str(self._p2)


class TestPoints(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Point(1, 1), Point(1, 1))

    def test_gte(self):
        self.assertGreaterEqual(Point(1, 1), Point(0, 0))

if __name__ == "__main__":
    unittest.main()
