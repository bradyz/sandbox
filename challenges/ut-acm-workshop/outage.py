def dfs(c):
    if c in vis:
        return

    vis.add(c)

    for y in g:
        if y in g[c]:
            dfs(y)

for _ in range(int(input())):
    u, v, w = map(int, input().split())
    g = {}

    for _ in range(u):
        x, y = input().split()
        g[x] = g.get(x, set()) | set([y])
        g[y] = g.get(y, set()) | set([x])

    for _ in range(v):
        x = input().strip()
        for y in g:
            g[y] = g[y] - set([x])

    for _ in range(w):
        x = input().strip()
        vis = set()
        dfs(x)
        vis -= set([x])

        if vis:
            print(" ".join(sorted(vis)))
        else:
            print("NONE")
