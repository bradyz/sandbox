def prim(g, p):
    r = []              # result edges
    s = [p[0].v]        # stack
    v = set([p[0].v])   # visited
    m = [[None for j in range(len(p))] for i in range(len(p))]

    # turn the graph into a matrix
    for e in g:
        m[e.a.v][e.b.v] = m[e.b.v][e.a.v] = e

    # dfs for minimum edge costs
    while s:
        b_v = None

        # look for the minimum edge from the vertex
        for i, e in enumerate(m[s[-1]]):
            if e and i not in v and (not b_v or (b_v and e.w < b_v.w)):
                b_v = e

        if b_v:
            # match - add edge to result
            v.add(b_v.to(s[-1]).v)
            s.append(b_v.to(s[-1]).v)
            r.append(b_v)
        else:
            # no match - backtrack
            s.pop()

    return r
