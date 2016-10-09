import heapq


def dijkstra(top):
    dist = [-1 for _ in range(top+1)]
    dist[top] = 0

    q = []
    heapq.heappush(q, (0, top))

    while q:
        w, u = heapq.heappop(q)

        for mult, cost in graph.items():
            if u % abs(mult) != 0:
                continue
            v = u + mult
            w_v = w + cost * abs(mult)
            if v >= 0 and v < top and (dist[v] == -1 or w_v < dist[v]):
                dist[v] = w_v
                heapq.heappush(q, (w_v, v))
                v += mult
                w_v += cost * abs(mult)

    return dist


for _ in range(int(input())):
    e, f, h = map(int, input().split())
    graph = dict()
    for _ in range(e):
        cost, mult, word = input().split()
        cost, mult = int(cost), int(mult)
        if word == "UP":
            mult = -mult
        graph[mult] = min(graph.get(mult, int(1e100)), cost)
    dist = dijkstra(f-1)
    r = 0
    for u in map(int, input().split()):
        if dist[u] == -1:
            r = -1
            break
        r = max(r, dist[u])
    if r != -1:
        print(r)
    else:
        print("IMPOSSIBLE")
