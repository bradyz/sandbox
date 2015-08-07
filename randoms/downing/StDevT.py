#!/usr/bin/env python3

# ---------
# StDevT.py
# ---------

# https://docs.python.org/3/library/statistics.html#statistics.stdev

from functools  import reduce
from math       import sqrt
from statistics import stdev, StatisticsError
from timeit     import timeit
from unittest   import main, TestCase

def func(c):
    if len(c) <= 1:
        raise StatisticsError
    mean = sum(c) / len(c)
    return (sum((x-mean) ** 2 for x in c) / (len(c)-1)) ** .5

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [func]

    def test_1 (self) :
        for f in self.a :
            self.assertEqual(f([2, 2]), 0)

    def test_2 (self) :
        for f in self.a :
            self.assertEqual(f([2, 3]), 0.7071067811865476)

    def test_3 (self) :
        for f in self.a :
            self.assertEqual(f([2, 2, 2]), 0)

    def test_4 (self) :
        for f in self.a :
            self.assertEqual(f([2, 3, 4]), 1)

    def test_5 (self) :
        for f in self.a :
            self.assertRaises(StatisticsError, f, [])

    def test_6 (self) :
        for f in self.a :
            self.assertRaises(StatisticsError, f, [2])

    def test_7 (self) :
        for f in self.a :
            print()
            print(f.__name__)
            t = timeit(f.__name__ + "(10000 * [2]) == 0", "from __main__ import " + f.__name__, number = 100)
            print("{:.2f} milliseconds".format(t * 1000))

if __name__ == "__main__" :
    main()
