from bisect import bisect_left as bl
from bisect import bisect_right as br


# nlogn solution - not fast enough for n = 10^6
def solve(c, k):
    for i in range(1, len(c)):
        c[i] += c[i-1]

    res = 0

    for i in range(len(c)):
        l = bl(c, c[i]+k, lo=i+1)
        r = br(c, c[i]+k)
        if c[i] == k:
            res += 1
        if l != r:
            res += r - l

    print(res)


# doesnt work at all
# (╯°□°）╯︵ ┻━┻
def solve1(c, k):
    n = set([k])
    r = 0

    for i in range(1, len(c)):
        c[i] += c[i-1]
        n.add(c[i]+k)

    for i in range(len(c)):
        if c[i] in n:
            r += 1
        if c[i] == k:
            r += 1

    print(r)


def solve2(c, k):
    from collections import Counter
    dp = Counter()
    dp[0] = 1
    j = 0
    r = 0
    for i in range(len(c)):
        if c[i] == "1":
            j += 1
        r += dp[j-k]
        dp[j] += 1
    print(r)

if __name__ == "__main__":
    find = int(input())
    values = input()
    solve2(values, find)
