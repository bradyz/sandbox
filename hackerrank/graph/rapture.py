INT_MAX = 10**9
N, E = map(int, input().split())
cost = {u: dict() for u in range(1, N+1)}
for _ in range(E):
    u, v, w = map(int, input().split())
    cost[u][v] = w
    cost[v][u] = w
dist = [INT_MAX for _ in range(N+1)]
dist[1] = 0
for _ in range(N-1):
    for u in range(1, N+1):
        if dist[u] == INT_MAX:
            continue
        for v in cost[u]:
            if cost[u][v] < dist[u]:
                dist[v] = min(dist[v], dist[u])
            else:
                dist[v] = min(dist[v], dist[u]+(cost[u][v]-dist[u]))
if dist[N] != INT_MAX:
    print(dist[N])
else:
    print("NO PATH EXISTS")
