n, m, k = map(int, input().split())
g = [[0 for _ in range(m)] for _ in range(n)]
v = set()
q = [list(map(int, input().split())) for _ in range(k)]
for q, rc, ai in reversed(q):
    if q == 1:
        for j in range(m):
            if (rc-1, j) not in v:
                v.add((rc-1, j))
                g[rc-1][j] = ai
    else:
        for i in range(n):
            if (i, rc-1) not in v:
                v.add((i, rc-1))
                g[i][rc-1] = ai
for l in g:
    print(" ".join(map(str, l)))
