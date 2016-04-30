def dfs(u):
    s = [u]
    vis = {u}
    while s:
        c = s.pop()
        can = False
        if c not in g:
            continue
        for v in g[c]:
            if v in vis:
                can = True
                continue
            vis.add(v)
            s.append(v)
        if can:
            return "SURVIVE"
    return "DEAD"


for _ in range(int(input())):
    e = int(input())
    g = dict()
    for _ in range(e):
        u, v = map(int, input().split())
        if u in g:
            g[u].append(v)
        else:
            g[u] = [v]
    print(dfs(1))
