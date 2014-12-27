from timeit import timeit
from random import randrange


if __name__ == "__main__":
    print 10
    a = [randrange(100) for x in range(10)]
    print a
    print timeit('10 in a')
