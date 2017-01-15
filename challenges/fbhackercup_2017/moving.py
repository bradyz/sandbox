INF = float("inf")


def solve(n, g, r):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                g[i][j] = min(g[i][j], g[i][k] + g[k][j])

    for u, v in r:
        if g[1][v] == INF or g[1][u] == INF:
            return -1

    dp = [[-1, -1] for _ in range(len(r))]

    u, v = r[0]
    dp[0][0] = g[1][u] + g[u][v]
    dp[0][1] = g[1][u]

    for i in range(1, len(r)):
        u, v = r[i-1]
        x, y = r[i]

        dp[i][0] = min(dp[i-1][0] + g[v][x] + g[x][y],
                       dp[i-1][1] + g[u][v] + g[v][x] + g[x][y],
                       dp[i-1][1] + g[u][x] + g[x][v] + g[v][y])
        dp[i][1] = min(dp[i-1][0] + g[v][x],
                       dp[i-1][1] + g[u][x] + g[x][v] + g[v][x],
                       dp[i-1][1] + g[u][v] + g[v][x])

    return dp[-1][0]


for i in range(1, int(input())+1):
    n, m, k = map(int, input().split())

    g = [[INF for _ in range(n+1)] for _ in range(n+1)]
    for u in range(1, n+1):
        g[u][u] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u][v] = w
        g[v][u] = w

    r = [list(map(int, input().split())) for _ in range(k)]

    print("Case #%d: %d" % (i, solve(n, g, r)))
