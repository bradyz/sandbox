# 75C: Modified GCD
# Start Time: 12:39 p.m. 5-1-15
# End Time: 2:09 p.m. 5-1-15

from collections import Counter
from bisect import bisect_right as br

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


# all the factors of a number in sqrt(n) time
def f(num):
    i = 1
    res = []
    while i * i <= num:
        if num % i == 0:
            res.append(num // i)
            if i != num // i:
                res.append(i)
        i += 1
    return sorted(res)


# O(n^1.5) tle at 1:30 p.m. 5-1-15
def solve(c, x, y):
    for i in range(y, x-1, -1):
        if i in saved and saved[i] != -1:
            return i

        if not Counter(pf(i)) - Counter(c):
            return i
        else:
            saved[i] = -1

    return -1


def solve1(c, x, y):
    res = c[br(c, y)-1]
    return res if res >= x else -1

if __name__ == "__main__":
    args = map(int, input().split())
    n1, n2 = args
    g = f(gcd(n1, n2))

    for _ in range(int(input())):
        r1, r2 = map(int, input().split())
        print(solve1(g, r1, r2))
