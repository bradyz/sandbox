from collections import defaultdict
import heapq


INF = int(1e9)


def dijkstra(graph, source, with_bathrooms):
    cost = {source: 0}
    queue = [(0, source)]

    while queue:
        u_cost, u = heapq.heappop(queue)

        if u in with_bathrooms:
            return cost[u]

        for v in graph.get(u, dict()):
            v_cost = u_cost + graph[u][v]
            if v not in cost or v_cost < cost[v]:
                cost[v] = v_cost
                heapq.heappush(queue, (v_cost, v))
    return cost


floors = int(input())
with_bathrooms = list(map(int, input().split()))[1:]
with_elevator = list(map(int, input().split()))[1:]
start = int(input())

graph = defaultdict(dict)

for u in with_elevator:
    for v in with_elevator:
        graph[u][v] = 15 + 5 * abs(u - v)
        graph[v][u] = 15 + 5 * abs(u - v)

for i in range(floors):
    graph[i][i+1] = min(graph[i].get(i+1, INF), 20)
    graph[i][i-1] = min(graph[i].get(i-1, INF), 10)


print(dijkstra(graph, start, with_bathrooms))
