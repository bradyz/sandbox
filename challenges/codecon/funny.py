def dfs(u):
    if u == b:
        return
    elif u < 0 or u > f:
        return
    for v in range(f+1):
        if g[u][v] and not vis[v]:
            vis[v] = True
            dfs(v)

f, e, a, b = map(int, input().split())
g = [[0 for _ in range(f+1)] for _ in range(f+1)]
for _ in range(e):
    x, y = map(int, input().split())
    for v in range(y, f+1, x):
        g[y][v] = 1
        g[v][y] = 1
    for v in range(y, -1, -x):
        g[y][v] = 1
        g[v][y] = 1
vis = [False for _ in range(f+1)]
vis[a] = True
dfs(a)
if vis[b]:
    print(1)
else:
    print(0)
