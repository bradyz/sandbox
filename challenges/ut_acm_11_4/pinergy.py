from sys import MAX_INT as INF


def solve(g, n, s):
    dp = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for u in g:
        for v, w in g[u]:
            dp[u][v] = w
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if dp[i][k] == INF or dp[k][j] == INF:
                    continue
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
                if dp[1][n] <= -s:
                    return True
    tmp = dp[1][n]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][k] == INF or dp[k][j] == INF:
                continue
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])
    if dp[1][n] < tmp:
        return True
    return False


for _ in range(int(input())):
    n, m, s = map(int, input().split())
    g = {i: list() for i in range(1, n+1)}
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, -w))
    if solve(g, n, s):
        print("YES")
    else:
        print("NO")
