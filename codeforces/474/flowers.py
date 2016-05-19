t, k = map(int, input().split())
q = [list(map(int, input().split())) for _ in range(t)]
n = max(max(x) for x in q) + 1
dp = [[0, 0] for _ in range(n)]
dp[1][0] = 1
dp[k][1] = 1
for i in range(1, n):
    dp[i][0] += dp[i-1][0] + dp[i-1][1]
    if i >= k:
        dp[i][1] += dp[i-k][0] + dp[i-k][1]
dp1 = [dp[i][0] + dp[i][1] for i in range(n)]
for i in range(1, n):
    dp1[i] = dp1[i] + dp1[i-1]
for a, b in q:
    print((dp1[b] - dp1[a-1]) % 1000000007)
