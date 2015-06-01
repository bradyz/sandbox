from sys import maxsize as INT_MAX


def bellmanford(src, g, n):
    dist = [INT_MAX for _ in range(n)]
    dist[src] = 0

    for _ in range(n):
        for u in range(n):
            for v in range(n):
                if g[u][v] != INT_MAX:
                    dist[v] = min(dist[v], dist[u] + g[u][v])

    print("Vertex\tDistance")
    for i in range(n):
        print(str(i)+"\t"+str(dist[i]))

if __name__ == "__main__":
    graph = [[0, -1, 4, INT_MAX, INT_MAX],
             [INT_MAX, 0, 3, 2, 2, INT_MAX],
             [INT_MAX, INT_MAX, 0,  INT_MAX, INT_MAX],
             [INT_MAX, 1, 5, 0, INT_MAX, INT_MAX],
             [INT_MAX, INT_MAX, INT_MAX, -3, 0]]

    bellmanford(0, graph, len(graph))
