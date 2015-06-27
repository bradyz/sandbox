n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [[0 for j in range(m+1)] for i in range(n+1)]
for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j == 0:
            continue
        if i == c[j-1]:
            dp[i][j] += 1
        if i-c[j-1] >= 0:
            dp[i][j] += dp[i-c[j-1]][j]
        dp[i][j] += dp[i][j-1]
print(dp[n][m])
