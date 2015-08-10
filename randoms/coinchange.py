n = 10
c = [2, 5, 3, 6]

dp = [[0 for j in c] for i in range(n+1)]

for i in range(n+1):
    for j in range(len(c)):
        if i == 0:
            continue
        if i - c[j] >= 0:
            dp[i][j] = max(dp[i][j], dp[i-c[j]][j]+1)
        if j-1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i][j-1])

print(dp)
print(dp[n][len(c)-1])
