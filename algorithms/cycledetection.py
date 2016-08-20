def search(u, g, vis, done):
    vis.add(u)
    for v in g.get(u, []):
        if v not in vis:
            return search(v, vis)
        elif not done[v]:
            return False
    done.add(v)
    return True


def has_cycle(g):
    vis = set()
    done = set()
    for u in g:
        if u in vis:
            continue
        if search(u, g, vis, done):
            return True
    return False
