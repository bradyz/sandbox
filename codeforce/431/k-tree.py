n, k, d = map(int, input().split())
dp = [[0 for j in range(2)] for i in range(105)]
dp[0][1] = 1

for i in range(1, n+1):
    for j in range(1, min(i, k)+1):
        dp[i][0] = (dp[i][0] + dp[i-j][j >= d]) % 1000000007
        dp[i][1] = (dp[i][1] + dp[i-j][1]) % 1000000007

print(dp[n][0])
