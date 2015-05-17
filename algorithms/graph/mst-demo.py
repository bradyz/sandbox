import matplotlib.pyplot as plt
from unionfind import edge, point
from kruskal import kruskal
from prim import prim

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
    mst = prim(graph, points)

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

    # plt.show()
