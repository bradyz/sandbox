# Given an integer N, print how many values X, 1 <= X <= N, such that
# (X - 1) ! % X == X - 1.

# TODO: write the proof that only primes satisfy this condition

from math import factorial


def solve(n):
    def test(k):
        return factorial(k-1) % k == k-1
    for i in range(1, n):
        if test(i):
            print(str(i))


def primes_under(n):
    sieve = [True for _ in range(n+1)]

    for i in range(2, n+1):
        for j in range(i+i, n+1, i):
            sieve[j] = False

    return " ".join(map(str, filter(lambda x: sieve[x], range(1, n+1))))

if __name__ == "__main__":
    print(primes_under(20))
