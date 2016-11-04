import sys
from bisect import bisect_left

sys.setrecursionlimit(10000)


def recur(prefix, lo, hi, memo, arr):
    if hi <= lo:
        return 0
    elif (lo, hi) in memo:
        return memo[(lo, hi)]
    val = prefix[hi] - prefix[lo]
    i = bisect_left(prefix, prefix[lo] + val // 2, lo, hi)
    if i == lo:
        i += 1
    result = 0
    while i < hi and prefix[i] - prefix[lo] == prefix[hi] - prefix[i]:
        result = max(result, recur(prefix, lo, i, memo, arr) + 1)
        result = max(result, recur(prefix, i, hi, memo, arr) + 1)
        i += 1
    memo[(lo, hi)] = result
    return result


def solve(c, n):
    prefix = list(c)
    for i in range(1, n):
        prefix[i] += prefix[i-1]
    print(recur(prefix, 0, n-1, dict(), c))


for _ in range(int(input())):
    n = int(input()) + 1
    c = [0] + list(map(int, input().split()))
    solve(c, n)
