import heapq


def dijkstra(graph, source):
    cost = {source: 0}
    queue = [(0, source)]
    while queue:
        u_cost, u = heapq.heappop(queue)
        for v in graph.get(u, dict()):
            v_cost = u_cost + graph[u][v]
            if v not in cost or v_cost < cost[v]:
                cost[v] = v_cost
                heapq.heappush(queue, (v_cost, v))
    return cost
