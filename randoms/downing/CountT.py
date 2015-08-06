#!/usr/bin/env python3

# ---------
# CountT.py
# ---------

from itertools import count
from unittest  import main, TestCase

# from Count import      \
#     my_count_iterator, \
#     my_count_generator

class my_count_iterator():
    def __init__(self, start=0, inc=1):
        self.cur = start
        self.inc = inc

    def __iter__(self):
        return self

    def __next__(self):
        j = self.cur
        self.cur += self.inc
        return j

def my_count_generator(start=0, inc=1):
    while True:
        yield start
        start += inc

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_count_iterator,
            my_count_generator,
            count]

    def test_1 (self) :
        for f in self.a :
            p = f()
            self.assertIs(iter(p), p)
            self.assertEqual(next(p), 0)
            self.assertEqual(next(p), 1)
            self.assertEqual(next(p), 2)

    def test_2 (self) :
        for f in self.a :
            p = f(2)
            self.assertIs(iter(p), p)
            self.assertEqual(next(p), 2)
            self.assertEqual(next(p), 3)
            self.assertEqual(next(p), 4)

    def test_3 (self) :
        for f in self.a :
            p = f(5, 2)
            self.assertIs(iter(p), p)
            self.assertEqual(next(p), 5)
            self.assertEqual(next(p), 7)
            self.assertEqual(next(p), 9)

if __name__ == "__main__" :
    main()
