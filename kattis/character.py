from math import factorial


def choose(n, k):
    return factorial(n) / (factorial(n - k) * factorial(k))


total = int(input())

print(int(sum([choose(total, i) for i in range(2, total+1)])))
