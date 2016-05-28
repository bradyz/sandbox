n = 21
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(1, n):
    dp[0][i] += dp[0][i-1]
for i in range(1, n):
    dp[i][0] += dp[i-1][0]
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n-1][n-1])
