from unionfind import edge


def prim(g, p):
    r = []              # result edges
    s = [p[0].v]        # stack
    v = set([])         # visited
    m = [[-1 for j in range(len(p))] for i in range(len(p))]

    # turn the graph into a matrix
    for e in g:
        m[e.a.v][e.b.v] = m[e.b.v][e.a.v] = e.w

    # dfs for minimum edge costs
    while s:
        b_v = 999
        b_p = None
        # look for the minimum edge from the vertex
        for i, j in enumerate(m[s[-1]]):
            if j > -1 and i not in v and j < b_v:
                b_v = j
                b_p = i
        if b_p:
            # match - add edge to result
            v.add(b_p)
            s.append(b_p)
            r.append((s[-1], b_p, b_v))
        else:
            # no match - backtrack
            s.pop()

    for i in range(len(r)):
        print()
        print(r[i][0], r[i][1], r[i][2])
        print()

        for j in range(len(g)):
            print(g[j].a.v, g[j].b.v, g[j].w)
            if r[i][0] == g[j].a.v and r[i][1] == g[j].b.v and r[i][2] == g[j].w:
                r[i] = g[j]

    return r
