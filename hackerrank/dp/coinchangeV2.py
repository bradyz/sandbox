n, m = map(int, input().split())
c = list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(m):
    for j in range(c[i], n+1):
        dp[j] += dp[j-c[i]]
print(dp[n])
