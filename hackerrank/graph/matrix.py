from queue import Queue


def min_path(u):
    # print(g)
    r = None
    while p[u] != u and g[u][p[u]] != -1:
        if not r or g[u][p[u]] < g[r][p[r]]:
            r = u
        u = p[u]
    tmp = g[r][p[r]]
    g[r][p[r]] = -1
    g[p[r]][r] = -1
    return tmp


def bfs(s):
    global r
    # print("bfs", u)
    q = Queue()
    p[s] = s
    q.put(s)
    while not q.empty():
        u = q.get()
        if u in c and p[u] != u:
            r += min_path(u)
            continue
        for v in g[u]:
            if p[v] != -1 or g[u][v] == -1:
                continue
            p[v] = u
            q.put(v)

if __name__ == "__main__":
    n, k = map(int, input().split())
    g = {u: dict() for u in range(n)}
    for _ in range(n-1):
        u, v, w = map(int, input().split())
        g[u][v] = w
        g[v][u] = w
    c = {int(input()) for _ in range(k)}
    r = 0
    p = [-1 for _ in range(n)]
    for u in c:
        bfs(u)
    print(r)
