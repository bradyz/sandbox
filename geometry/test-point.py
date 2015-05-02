import unittest
from point import Point, Line


class TestPoint(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Point(1, 1), Point(1, 1))

    def test_gte(self):
        self.assertGreaterEqual(Point(1, 1), Point(0, 0))


class TestLine(unittest.TestCase):

    # ****************************************
    # *             point_given              *
    # ****************************************

    def test_point_given_x(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_x(2))

    def test_point_given_x_vertical(self):
        a = Line(Point(0, 0), Point(0, 5))
        self.assertEqual(None, a.point_given_x(2))

    def test_point_given_y(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_y(2))

    def test_point_given_y_vertical(self):
        a = Line(Point(0, 0), Point(0, 5))
        self.assertEqual(None, a.point_given_y(2))

    # ****************************************
    # *                 on                   *
    # ****************************************

    def test_on_true(self):
        a = Point(2, 2)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.on(b))

    def test_on_false(self):
        a = Point(0, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertFalse(a.on(b))

    # ****************************************
    # *             left_of                  *
    # ****************************************

    def test_left_of(self):
        a = Point(0, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.left_of(b))

    def test_left_of_on(self):
        a = Point(2, 2)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.left_of(b))

    def test_left_of_false(self):
        a = Point(2, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertFalse(a.left_of(b))

    # ****************************************
    # *             right_of                 *
    # ****************************************

    def test_right_of(self):
        a = Point(2, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.right_of(b))

    def test_right_of_on(self):
        a = Point(2, 2)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.right_of(b))

    def test_right_of_false(self):
        a = Point(0, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertFalse(a.right_of(b))

if __name__ == "__main__":
    unittest.main(verbosity=2)
