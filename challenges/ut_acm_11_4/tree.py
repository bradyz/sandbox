for _ in range(int(input())):
    n = int(input())
    g = dict()
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u] = g.get(u, set()) | {v}
        g[v] = g.get(v, set()) | {u}
    q = set(g.keys())
    for u in g:
        if len(g[u]) > 1:
            q.remove(u)
    left = set(g.keys())
    r = list()
    while len(left) > 2:
        u = min(q)
        # print(q, u)
        q.remove(u)
        left.remove(u)
        for v in g[u]:
            r.append(v)
            g[v].remove(u)
            if len(g[v]) == 1:
                q.add(v)
    print(" ".join(map(str, r)))
