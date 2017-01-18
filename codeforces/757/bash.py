from math import sqrt


def prime_factors(x):
    r = int(sqrt(x)) + 1
    for i in range(2, r):
        while x % i == 0:
            yield i
            x //= i
    if x > 1:
        yield x


n = int(input())
c = list(map(int, input().split()))
d = dict()

for v in c:
    print(" ".join(map(str, prime_factors(v))))
    for x in set(prime_factors(v)):
        d[x] = d.get(x, 0) + 1

print(max(1, max(d.values())))
