from queue import Queue


RIGHT = 1000
S = "SOURCE"
T = "SINK"
INF = float('inf')


def bfs(p, r):
    q = Queue()
    q.put(S)
    while not q.empty():
        u = q.get()
        for v in r.get(u, []):
            if v in p or r[u][v] <= 0:
                continue
            p[v] = u
            q.put(v)
    return (T in p)


def max_flow(r):
    m = 0
    p = dict()
    while bfs(p, r):
        # Bottleneck.
        u = T
        b = INF
        while u != S:
            b = min(b, r[p[u]][u])
            u = p[u]
        # Update.
        u = T
        while u != S:
            r[u][p[u]] += b
            r[p[u]][u] -= b
            u = p[u]
        # Add flow, clear vis.
        m += b
        p = dict()
    return m


for _ in range(int(input())):
    n, t, m = map(int, input().split())
    r = {S: dict(), T: dict()}
    for u in range(1, n+1):
        r[u] = dict()
        r[u][S] = 0
        r[S][u] = t
        r[RIGHT + u] = dict()
        r[RIGHT + u][T] = 1
        r[T][RIGHT + u] = 0
    for _ in range(m):
        u, v = map(int, input().split())
        r[u][RIGHT + v] = 1
        r[RIGHT + v][u] = 0
        r[v][RIGHT + u] = 1
        r[RIGHT + u][v] = 0
    print(max_flow(r))
