import heapq


def dijkstra(graph, source):
    cost = {source: 0}
    queue = [(0, source)]

    while queue:
        u_cost, u = heapq.heappop(queue)

        for v, s, e, t in graph.get(u, dict()):
            if u_cost > e:
                continue

            v_cost = max(s, u_cost) + t

            if v not in cost or v_cost < cost[v]:
                cost[v] = v_cost
                heapq.heappush(queue, (v_cost, v))

    return cost


m, c = map(int, input().split())
src, dst = input().split()
graph = {input(): list() for _ in range(m)}

for _ in range(c):
    a, b, s, e, t = input().split()
    s = int(s)
    e = int(e)
    t = int(t)

    graph[a].append((b, s, e, t))


cost = dijkstra(graph, src)

print(cost.get(dst, None) or 'TRAPPED!')
