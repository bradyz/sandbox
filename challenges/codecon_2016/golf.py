n = int(input())
g = list(map(int, input().split()))
m = int(input())
h = list(map(int, input().split()))
f = max(h) + max(g)
dp = [[False for _ in range(n+1)] for _ in range(f+1)]
for i in range(n+1):
    dp[0][i] = True
for i in range(1, f+1):
    for j in range(1, n+1):
        if i - g[j-1] >= 0 and dp[i-g[j-1]][j]:
            dp[i][j] = True
        elif dp[i][j-1]:
            dp[i][j] = True
for x in h:
    can = False
    for y in g:
        if dp[x+y][n]:
            print("yes")
            can = True
            break
    if not can:
        print("no")
# for i in range(len(dp)):
#     print(i, dp[i])
# print(h)
