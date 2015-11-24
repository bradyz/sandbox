n = int(input())
c = [int(input()) for _ in range(n)]
dp = [1 for _ in range(n)]
for i in range(1, n):
    if c[i] > c[i-1]:
        dp[i] = dp[i-1]+1
for i in range(n-2, -1, -1):
    if c[i] > c[i+1]:
        dp[i] = max(dp[i+1]+1, dp[i])
print(sum(dp))
