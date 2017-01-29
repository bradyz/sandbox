best_path = list()


def most(start, passes, graph, visited=set(), path=list()):
    global best_path
    if not visited:
        visited.add(start)
        path.append(start)
    for neighbor, color, amount in graph.get(start, set()):
        if passes.get(color, 0) >= amount and neighbor not in visited:
            passes[color] -= amount
            visited.add(neighbor)
            path.append(neighbor)
            most(neighbor, passes, graph, visited, path)
            if len(path) > len(best_path):
                best_path = type(path)(path)
            path.pop()
            visited.remove(neighbor)
            passes[color] += amount


c, r = map(int, input().split())
start = input()
passes = dict()
for _ in range(c):
    color, amount = input().split()
    passes[color] = int(amount)
graph = dict()
for _ in range(r):
    u, v, color, amount = input().split()
    if u not in graph:
        graph[u] = list()
    if v not in graph:
        graph[v] = list()
    graph[v].append((u, color, int(amount)))
    graph[u].append((v, color, int(amount)))
most(start, passes, graph)
print(" ".join(best_path))
