n = int(input())
c = [int(input()) for _ in range(n)]

dp = [[False for _ in range(n)] for _ in range(2005)]

for i in range(n):
    dp[0][i] = True

dp[c[0]][0] = True

for i in range(1, 2005):
    for j in range(1, n):
        if i - c[j] >= 0 and dp[i - c[j]][j-1]:
            dp[i][j] = True
        dp[i][j] |= dp[i][j-1]

r = 0

for i in range(2005):
    if dp[i][n-1] and abs(1000 - i) <= abs(1000 - r):
        r = i

print(r)
