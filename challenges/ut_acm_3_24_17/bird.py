import heapq


def dijkstra(graph, src, dst):
    dist = {src: 0}
    q = [(0, src)]

    while q:
        w, u = heapq.heappop(q)
        for v in graph.get(u, dict()):
            nw = w + graph[u][v]
            if v not in dist or nw < dist[v]:
                dist[v] = nw
                heapq.heappush(q, (nw, v))

    return dist.get(dst, "not possible")


for _ in range(int(input())):
    src, dst = map(int, input().split())
    graph = dict()

    for _ in range(int(input())):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = dict()
        if w <= 90:
            graph[u][v] = w

    print(dijkstra(graph, src, dst))
