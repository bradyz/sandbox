import heapq


def dijkstra(graph, src, n):
    dist = [-1 for _ in range(n)]
    dist[src] = 0
    q = [(0, src)]
    while q:
        w, u = heapq.heappop(q)
        for v in range(n):
            if graph[u][v] == 0:
                continue
            nw = w + graph[u][v]
            if dist[v] == -1 or nw < dist[v]:
                dist[v] = nw
                heapq.heappush(q, (nw, v))
    for i in range(n):
        print(i, dist[i])
    return dist


if __name__ == "__main__":
    adj_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 0, 10, 0, 2, 0, 0],
                 [0, 0, 0, 14, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]
    dijkstra(adj_graph, 0, len(adj_graph))
