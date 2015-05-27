import matplotlib.pyplot as plt
from unionfind import edge, point
from kruskal import kruskal
from prim import prim


def setup():
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

    return graph, points


# g => graph
# p => points
def plot_base(g, p):
    # plot all points
    for v in points:
        plt.plot(v.x, v.y, "ro")

    # plot all edges
    for e in g:
        c = e.tuple_rep()
        plt.plot([x[0] for x in c], [x[1] for x in c], "b--")


# m => set of edges in mst
def plot_mst(m):
    for e in m:
        c = e.tuple_rep()
        plt.plot([x[0] for x in c], [x[1] for x in c], "b-")

if __name__ == "__main__":
    # base data
    graph, points = setup()

    # find the mst
    mst_prim = prim(graph, points, len(points))
    mst_kruskal = kruskal(graph)

    # metadata for Kruskal
    p1 = plt.subplot(221)
    p1.set_title("Kruskal")
    plt.ylim([-1, 5])
    plt.xlim([-1, 5])

    # basic
    plot_base(graph, points)

    # the goods
    plot_mst(mst_kruskal)

    # metadata for Prim
    p2 = plt.subplot(222)
    p2.set_title("Prim")
    plt.ylim([-1, 5])
    plt.xlim([-1, 5])

    # basic
    plot_base(graph, points)

    # the goods
    plot_mst(mst_prim)

    plt.show()
