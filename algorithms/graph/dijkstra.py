from sys import maxsize as INT_MAX


# O(V^2) time complexity
def dijkstra(graph, src, n):
    # returns the minimum closest vertex not yet visited
    def min_dist():
        min_v = INT_MAX
        min_i = -1

        for i in range(n):
            if not spt[i] and dist[i] < min_v:
                min_v = dist[i]
                min_i = i

        return min_i

    dist = [INT_MAX for _ in range(n)]
    spt = [False for _ in range(n)]

    dist[src] = 0

    for i in range(n):
        u = min_dist()
        spt[u] = True

        for v in range(n):
            if not spt[v] and graph[u][v] and dist[u]+graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    # print distances from source
    for i in range(n):
        print(i, dist[i])

if __name__ == "__main__":
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 0, 10, 0, 2, 0, 0],
             [0, 0, 0, 14, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    dijkstra(graph, 0, len(graph))
