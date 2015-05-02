import unittest
from point import Point, Line


class TestPoint(unittest.TestCase):

    def test_equality(self):
        self.assertEqual(Point(1, 1), Point(1, 1))

    def test_gte(self):
        self.assertGreaterEqual(Point(1, 1), Point(0, 0))


class TestLine(unittest.TestCase):

    def test_point_given_x(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_x(2))

    def test_point_given_x_vertical(self):
        a = Line(Point(0, 0), Point(0, 5))
        print(a.point_given_x(2))
        self.assertEqual(None, a.point_given_x(2))

    def test_point_given_y(self):
        a = Line(Point(0, 0), Point(5, 5))
        self.assertEqual(Point(2, 2), a.point_given_y(2))

    def test_point_given_y_vertical(self):
        a = Line(Point(0, 0), Point(0, 5))
        self.assertEqual(None, a.point_given_y(2))

    def test_left_of(self):
        a = Point(0, 1)
        b = Line(Point(0, 0), Point(1, 1))
        self.assertTrue(a.left_of(b))

    @unittest.skip("not implemented")
    def test_left_of_horizontal(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=2)
