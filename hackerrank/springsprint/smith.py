import sys


def primes(n):
    pf = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            pf.append(d)
            n //= d
        d += 1
    if n > 1:
        pf.append(n)
    return pf


def is_smith(n):
    pf = primes(n)
    pf = map(str, pf)
    p = 0
    for val in pf:
        for num in val:
            p += int(num)
    if p == sum([int(x) for x in str(n)]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        num = int(line)
        print(is_smith(num))
