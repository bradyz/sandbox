INF = float(1e10)

howie_room, connections = map(int, input().split())
graph = dict()

for _ in range(connections):
    u, v, w = map(int, input().split())

    if u not in graph:
        graph[u] = list()

    graph[u].append((v, w))

start = set()
edge_to = dict()
slowest = dict()
fastest = dict()

for u in graph:
    for v, _ in graph[u]:
        start.add(u)
        start.add(v)

        edge_to[v] = edge_to.get(v, 0) + 1

        slowest[u] = -INF
        slowest[v] = -INF

        fastest[u] = INF
        fastest[v] = INF

for u in graph:
    for v, _ in graph[u]:
        if v in start:
            start.remove(v)

for u in start:
    slowest[u] = 0
    fastest[u] = 0

stack = list(start)

while stack:
    u = stack.pop()

    for v, w in graph.get(u, dict()):
        fastest[v] = min(fastest[v], fastest[u] + w)
        slowest[v] = max(slowest[v], slowest[u] + w)

        edge_to[v] -= 1

        if edge_to[v] == 0:
            stack.append(v)

print(fastest[howie_room], slowest[howie_room])
