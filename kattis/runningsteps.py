# 4 * a + 2 * b = k
# a >= b
# after we find a, b we have essentially a binary string for a single leg
# a = 3
# b = 2
# 11100
# we find the number of permutations of a set w/ repeated elements
# (a + b)! / (a! b!)
# then multiply this by the number of the right leg, which is the same
from math import factorial


def solve(k):
    result = 0

    for b in range(101):
        a = (k - 2 * b) / 4

        if float(a) != int(a):
            continue
        elif a < b:
            continue

        a = int(a)

        n = factorial(a + b) // (factorial(a) * factorial(b))

        result += n * n

    return result


for t in range(1, int(input()) + 1):
    _, k = map(int, input().split())

    print('%d %d' % (t, solve(k)))
