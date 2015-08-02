import unittest
import numpy as np
from convexhullV2 import cw_turn, ccw_turn, colinear


class TestTurnOrientation(unittest.TestCase):

    def test_cwturn1(self):
        a = [1, 1]
        b = [2, 2]
        c = [3, 1]
        d = np.array([a, b, c], np.int32)
        self.assertTrue(cw_turn(d))

    def test_colinear1(self):
        a = [1, 1]
        b = [2, 2]
        c = [3, 3]
        d = np.array([a, b, c], np.int32)
        self.assertTrue(colinear(d))

    def test_ccwturn1(self):
        a = [1, 1]
        b = [2, 2]
        c = [3, 4]
        d = np.array([a, b, c], np.int32)
        self.assertTrue(ccw_turn(d))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestTurnOrientation)
    unittest.TextTestRunner(verbosity=2).run(suite)
