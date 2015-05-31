# 189A: Cut Ribbon
# Start Time: 10:18 a.m. 4-28-15
# End Time: 10:50 a.m. 4-28-15


def solve(n, c):
    dp = [-1 for _ in range(n + 1)]
    for i in range(len(c)):
        for j in range(n+1):
            if j == 0:
                dp[j] = 0
            elif j - c[i] >= 0 and dp[j-c[i]] >= 0:
                dp[j] = max(dp[j-c[i]] + 1, dp[j])

    return dp[n]

args = list(map(int, input().split()))
length = args[0]
vals = args[1:]

print(solve(length, vals))
