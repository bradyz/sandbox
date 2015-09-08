def solve():
    def dfs(c):
        if c == v:
            return True

        r = False

        for i in range(1, n+1):
            if g[w][c][i] and i not in p:
                p[i] = c
                r |= dfs(i)

        return r

    n, m = map(int, input().split())
    g = [[[False for j in range(n+1)] for i in range(n+1)] for _ in range(m+1)]

    for _ in range(m):
        u, v, w = map(int, input().split())
        g[w][u][v] = True
        g[w][v][u] = True

    for _ in range(int(input())):
        u, v = map(int, input().split())
        res = 0

        for w in range(1, m+1):
            p = dict()
            p[u] = -1
            res += dfs(u)

        print(res)

solve()
