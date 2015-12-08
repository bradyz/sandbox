from queue import PriorityQueue


N, E = map(int, input().split())
cost = {u: dict() for u in range(1, N+1)}

for _ in range(E):
    u, v, w = map(int, input().split())
    cost[u][v] = w
    cost[v][u] = w

dist = [-1 for _ in range(N+1)]
dist[1] = 0

que = PriorityQueue()
que.put((dist[1], 1))

while not que.empty():
    u = que.get()[1]
    if u == N:
        break
    for v in cost[u]:
        if dist[v] == -1 or dist[u] + max(0, cost[u][v]-dist[u]) < dist[v]:
            dist[v] = dist[u] + max(0, cost[u][v]-dist[u])
            que.put((dist[v], v))

if dist[N] != -1:
    print(dist[N])
else:
    print("NO PATH EXISTS")
