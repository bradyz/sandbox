from unionfind import edge, union, find


def kruskal(g):
    # number of vertices
    v = len(set([x._a for x in g]) | set([x._b for x in g]))

    # disjoin union data structure for subsets
    p = [-1 for _ in range(v)]

    # result set of edges
    res = []

    # add disjoint edges by weight
    for e in sorted(g, key=lambda x: x._w):
        if find(p, e._a) != find(p, e._b):
            res.append(e)
            union(p, e._a, e._b)

    for e in res:
        print(e)

if __name__ == "__main__":
    graph = []
    graph.append(edge(7, 6, 1))
    graph.append(edge(8, 2, 2))
    graph.append(edge(6, 5, 2))
    graph.append(edge(0, 1, 4))
    graph.append(edge(2, 5, 4))
    graph.append(edge(8, 6, 6))
    graph.append(edge(2, 3, 7))
    graph.append(edge(7, 8, 7))
    graph.append(edge(0, 7, 8))
    graph.append(edge(1, 2, 8))
    graph.append(edge(3, 4, 9))
    graph.append(edge(5, 4, 10))
    graph.append(edge(1, 7, 11))
    graph.append(edge(3, 5, 14))
    kruskal(graph)
