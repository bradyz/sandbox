n, r, c = map(int, input().split())
if n > r * c:
    print(-1)
else:
    g = [[0 for _ in range(c)] for _ in range(r)]
    ret = 1
    for i in range(r):
        for j in range(c):
            if ret > n:
                continue
            g[i][j] = ret
            ret += 1
    for i in range(1, r):
        if (g[i][0] % 2) == (g[i-1][0] % 2):
            g[i] = list(reversed(g[i]))
    for l in g:
        print(" ".join(map(str, l)))
