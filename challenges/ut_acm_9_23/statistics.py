from queue import Queue


def bfs(u, g, vis):
    q = Queue()
    q.put(u)
    vis.add(u)
    blob = set([u])
    while not q.empty():
        x = q.get()
        blob.add(x)
        for v in g.get(x, set()):
            if v in vis:
                continue
            vis.add(v)
            q.put(v)
    return blob



for t in range(int(input())):
    n, p, c = map(int, input().split())
    g = {x: set() for x in range(p)}
    for _ in range(c):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)
    blobs = list()
    vis = set()
    for u in g:
        if u in vis:
            continue
        blobs.append(bfs(u, g, vis))
    blobs.sort(key=lambda x: -len(x))
    r = 0
    t = 0
    for blob in blobs:
        if t >= n:
            break
        r += 1
        t += len(blob)
    if t >= n:
        print(r)
    else:
        print("IMPOSSIBLE")
