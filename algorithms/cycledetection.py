def search(u, g, vis, done, cycle):
    vis.add(u)
    for v in g.get(u, []):
        in_cycle = False
        if v not in vis and search(v, g, vis, done, cycle):
            in_cycle = True
        elif v not in done:
            in_cycle = True
        if in_cycle:
            done.add(u)
            cycle.add(v)
            return True
    done.add(u)
    return False


def has_cycle(g):
    vis = set()
    done = set()
    cycles = list()
    cycle = set()
    for u in g:
        if u in vis:
            continue
        cycles.append(set())
        search(u, g, vis, done, cycles[-1])
    return cycles


if __name__ == "__main__":
    e = int(input())
    g = dict()
    for _ in range(e):
        u, v = map(int, input().split())
        if u not in g:
            g[u] = list()
        g[u].append(v)
    print(has_cycle(g))
