for _ in range(int(input())):
    g = dict()
    p = set()
    x = set()

    for _ in range(int(input())):
        u, v = input().split()
        g[u] = g.get(u, set()) | set([v])
        g[v] = g.get(v, set()) | set([u])

        p.add(u)
        p.add(v)

    for v in p:
        if v not in g:
            g[v] = []

    groups = []

    for v in sorted(p, key=lambda x: -len(g[x])):
        if v in x:
            continue
        group = set([v])
        not_allowed = set(g[v])
        for u in sorted(p, key=lambda x: -len(g[x])):
            if u != v and u not in x and not (g[u] & group) \
                    and not (group & g[u]):
                t = True
                x.add(u)
                group.add(u)
        groups.append(group)

    print(len(groups))
