from unionfind import union, find


def kruskal(g):
    # number of vertices
    v = len(set([x.a for x in g]) | set([x.b for x in g]))

    # disjoin union data structure for subsets
    p = [-1 for _ in range(v)]

    # result set of edges
    res = []

    # add disjoint edges by weight
    for e in sorted(g, key=lambda x: x.w):
        if find(p, e.a.v) != find(p, e.b.v):
            res.append(e)
            union(p, e.a.v, e.b.v)

    return res
