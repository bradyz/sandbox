from sys import maxsize as INT_MAX


for t in range(1, INT_MAX):
    n = int(input())
    if n == 0:
        break
    g = [[INT_MAX for _ in range(n+1)] for _ in range(n+1)]
    p = [[i for j in range(n+1)] for i in range(n+1)]
    for u in range(n):
        u = u + 1
        out = list(map(int, input().split()))[1:]
        for i in range(0, len(out), 2):
            v, w = out[i], out[i+1]
            g[u][v] = w
    s, e = map(int, input().split())
    input()
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][k]+g[k][j] < g[i][j]:
                    g[i][j] = g[i][k]+g[k][j]
                    p[i][j] = p[k][j]

    def path(i, j):
        if i != j:
            for x in path(i, p[i][j]):
                yield x
        yield str(j)

    res = "Case " + str(t) + ": Path = " + " ".join(p for p in path(s, e))
    res += "; " + str(g[s][e]) + " second delay"
    print(res)
