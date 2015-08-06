#!/usr/bin/env python3

# ---------
# RangeT.py
# ---------

from unittest import main, TestCase

# from Range import      \
    # my_range_iterator, \
    # my_range_generator

class my_range_iterator:
    class A:
        def __init__(self, start, end):
            self.cur = start
            self.end = end

        def __iter__(self):
            return self
        
        def __next__(self):
            if self.cur >= self.end:
                raise StopIteration
            j = self.cur 
            self.cur += 1
            return j

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self.A(self.start, self.end)

def blah(start, end):
    def f():
        a = start
        while a < end:
            yield a
            a += 1
    return f

class my_range_generator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        s = self.start
        while s < self.end:
            yield s
            s += 1

class MyUnitTests (TestCase) :
    def setUp (self) :
        self.a = [
            my_range_iterator,
            my_range_generator,
            range]

    def test_1 (self) :
        for f in self.a :
            x = f(2, 2)
            self.assertEqual(list(x), [])
            self.assertEqual(list(x), [])

    def test_2 (self) :
        for f in self.a :
            x = f(2, 3)
            self.assertEqual(list(x), [2])
            self.assertEqual(list(x), [2])

    def test_3 (self) :
        for f in self.a :
            x = f(2, 4)
            self.assertEqual(list(x), [2, 3])
            self.assertEqual(list(x), [2, 3])

    def test_4 (self) :
        for f in self.a :
            x = f(2, 5)
            self.assertEqual(list(x), [2, 3, 4])
            self.assertEqual(list(x), [2, 3, 4])

if __name__ == "__main__" :
    main()
