import sys
from bisect import bisect

e = 1e-6


def binary_search(x):
    if x >= cost[N-1]:
        return binary_search(x - cost[N-1])
    i = bisect(cost, x)
    if i == 0:
        return x
    return x - cost[i-1]

if __name__ == "__main__":
    sys.setrecursionlimit(10000)

    for T in range(int(input())):
        N, A, B = map(int, input().split())
        cost = list(map(int, input().split()))

        for i in range(1, N):
            cost[i] += cost[i-1]

        result = 0

        for x in range(A, B+1):
            if x != A:
                result += round(binary_search(x-e))
            if x != B:
                result += round(binary_search(x+e))

        print(result)
        print(result / (2 * B - 2 * A))
