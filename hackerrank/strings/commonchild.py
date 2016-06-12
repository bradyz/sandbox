a = input()
b = input()
n = len(a)
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = int(a[0] == b[0])
for i in range(1, n):
    dp[i][0] = max(dp[i-1][0], int(a[i] == b[0]))
for i in range(1, n):
    dp[0][i] = max(dp[0][i-1], int(b[i] == a[0]))
for i in range(1, n):
    for j in range(1, n):
        if a[i] == b[j]:
            dp[i][j] = max(1 + dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# print("\n".join(map(str, dp)))
print(max(map(lambda x: max(x), dp)))
