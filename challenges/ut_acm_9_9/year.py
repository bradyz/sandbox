from queue import Queue

def bfs(g, dist, u):
    vis = set()
    q = Queue()
    vis.add(u)
    q.put((u, 0))
    while not q.empty():
        cur, d = q.get()
        dist[u][cur] = d
        for v in g.get(cur, []):
            if v in vis:
                continue
            vis.add(v)
            q.put((v, d+1))


for _ in range(int(input())):
    a, f = map(int, input().split())
    g = {i: list() for i in range(a)}
    dist = {i: dict() for i in range(a)}
    for i in range(f):
        u, v = map(int, input().split())
        g[u].append(v)
    for u in range(a):
        bfs(g, dist, u)
    cannot = False
    r = -1
    for u in range(a):
        for v in range(a):
            b1 = dist.get(u, dict())
            b2 = dist.get(v, dict())
            same = set(b1.keys()) & set(b2.keys())
            if not same:
                cannot = True
                continue
            min_same = int(1e9)
            for w in same:
                min_same = min(min_same, max(dist[u][w], dist[v][w]))
            r = max(r, min_same)
    if cannot:
        print("IMPOSSIBLE")
    else:
        print(r)
