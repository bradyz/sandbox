import matplotlib.pyplot as plt
from unionfind import edge, point, union, find


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

if __name__ == "__main__":
    p_0 = point(0, 0, 1)
    p_1 = point(1, 1, 2)
    p_2 = point(2, 2, 2)
    p_3 = point(3, 3, 2)
    p_4 = point(4, 4, 1)
    p_5 = point(5, 3, 0)
    p_6 = point(6, 2, 0)
    p_7 = point(7, 1, 0)
    p_8 = point(8, 2, 1)

    points = [p_0, p_1, p_2, p_3, p_4, p_5, p_6, p_7, p_8]

    # ugly but it'll work for now
    graph = [edge(p_7, p_6, 1), edge(p_8, p_2, 2), edge(p_6, p_5, 2),
             edge(p_0, p_1, 4), edge(p_2, p_5, 4), edge(p_8, p_6, 6),
             edge(p_2, p_3, 7), edge(p_7, p_8, 7), edge(p_0, p_7, 8),
             edge(p_1, p_2, 8), edge(p_3, p_4, 9), edge(p_5, p_4, 10),
             edge(p_1, p_7, 11), edge(p_3, p_5, 14)]

    # find the mst
    mst = kruskal(graph)

    # metadata
    plt.suptitle("Kruskal's MST")
    plt.ylim([-1, 5])
    plt.xlim([-1, 5])

    # plot all points
    for p in points:
        plt.plot(p.x, p.y, "ro")

    # plot all edges
    for e in graph:
        c = e.tuple_rep()
        plt.plot([x[0] for x in c], [x[1] for x in c], "b--")

    # plot mst edges
    for e in mst:
        c = e.tuple_rep()
        plt.plot([x[0] for x in c], [x[1] for x in c], "b-")

    plt.show()
