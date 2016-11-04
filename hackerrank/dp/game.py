from bisect import bisect_left


def recur(prefix, lo, hi, memo, arr):
    if (lo, hi) in memo:
        return memo[(lo, hi)]
    val = prefix[hi] - prefix[lo]
    if val % 2 != 0:
        memo[(lo, hi)] = 0
        return 0
    i = bisect_left(prefix, prefix[lo] + val // 2, lo, hi) + 1
    if i >= hi:
        return 0
    print(lo, hi, i, c[lo:i], c[i:hi+1])
    result = max(recur(prefix, lo, i, memo, arr), recur(prefix, i-1, hi, memo, arr)) + 1
    memo[(lo, hi)] = result
    return result


def solve(c, n):
    prefix = list(c)
    for i in range(1, n):
        prefix[i] += prefix[i-1]
    print(prefix)
    print(recur(prefix, 0, n-1, dict(), c))


for _ in range(int(input())):
    n = int(input()) + 1
    c = [0] + list(map(int, input().split()))
    solve(c, n)
