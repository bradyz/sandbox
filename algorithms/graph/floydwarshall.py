from copy import deepcopy
from sys import maxsize as INF


# O(V^3) time, O(V^2) space, O(1) lines to implement
def floydwarshall(n, g):
    w = deepcopy(g)
    p = [[[] for _ in range(n)] for _ in range(n)]

    # dp away
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if w[i][k]+w[k][j] < w[i][j]:
                    w[i][j] = w[i][k]+w[k][j]
                    p[i][j] = p[i][k]+[k]

    # print("\n".join(map(str, p)))
    # print("\n".join(map(str, w)))

    return w

if __name__ == "__main__":
    num_nodes, num_edges = map(int, input().split())
    graph = [[INF for j in range(num_nodes)] for i in range(num_nodes)]

    # the distance from a node to itself is 0
    for i in range(num_nodes):
        graph[i][i] = 0

    # populate adjacency matrix
    for _ in range(num_edges):
        u, v, w = map(int, input().split())
        graph[u][v] = w

    min_dist_graph = floydwarshall(num_nodes, graph)
