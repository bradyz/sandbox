# 75C: Modified GCD
# Start Time: 12:39 p.m. 5-1-15
# End Time: 10:50 a.m. 4-28-15

from math import sqrt, ceil
from collections import Counter

saved = {}


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def pf(num):
    i = 2
    ps = []

    while num > 1:
        if num % i == 0:
            num //= i
            ps.append(i)
        else:
            i += 1

    return ps


def solve(c, x, y):
    for i in range(y, x-1, -1):
        if i in saved and saved[i] != -1:
            return i

        if not Counter(pf(i)) - Counter(c):
            return i
        else:
            saved[i] = -1
    return -1

if __name__ == "__main__":
    args = map(int, input().split())
    n1, n2 = args
    g = pf(gcd(n1, n2))

    for _ in range(int(input())):
        r1, r2 = map(int, input().split())
        print(solve(g, r1, r2))
