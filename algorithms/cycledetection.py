def search(u, g, vis, done):
    vis.add(u)
    for v in g.get(u, []):
        if v not in vis and search(v, g, vis, done):
            return True
        elif v not in done:
            return True
    done.add(u)
    return False


def has_cycle(g):
    vis = set()
    done = set()
    for u in g:
        if u in vis:
            continue
        if search(u, g, vis, done):
            return True
    return False


if __name__ == "__main__":
    e = int(input())
    g = dict()
    for _ in range(e):
        u, v = map(int, input().split())
        if u not in g:
            g[u] = list()
        g[u].append(v)
    print(has_cycle(g))
