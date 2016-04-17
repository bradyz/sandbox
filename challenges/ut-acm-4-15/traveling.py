from queue import Queue


def longest_branch(u):
    s = [(1, 0)]
    v = {1}
    m = 0
    while s:
        c, w = s.pop()
        if not g[c]:
            m = max(m, w)
            continue
        for x in g[c]:
            if x in v:
                continue
            v.add(x)
            s.append((x, g[c][x] + w))
    return m


for _ in range(int(input())):
    n = int(input())
    g = {i: dict() for i in range(1, n+1)}
    e = list()
    for _ in range(n-1):
        x, y, w = map(int, input().split())
        e.append((x, y, w))
        g[x][y] = w
        g[y][x] = w
    new_g = {i: dict() for i in range(1, n+1)}

    q = Queue()
    q.put(1)
    v = {1}

    while not q.empty():
        c = q.get()
        for u in g[c]:
            if u in v:
                continue
            v.add(u)
            q.put(u)
            new_g[c][u] = g[c][u]

    g = new_g

    mst = sum(w[2] for w in e)

    print(mst * 2 - longest_branch(1))
