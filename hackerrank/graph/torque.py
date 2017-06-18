def dfs(u, visited, found):
    found.append(u)

    for v in graph.get(u, list()):
        if v in visited:
            continue

        visited.add(v)
        dfs(v, visited, found)


def solve():
    if m == 0:
        return n * lib
    elif lib < road:
        return n * lib

    connected = list()
    visited = set()

    for u in graph:
        if u in visited:
            continue

        visited.add(u)

        found = list()
        dfs(u, visited, found)

        connected.append(found)

    result = 0

    for comp in connected:
        result += (len(comp) - 1) * road + lib

    return result + (n - len(visited)) * lib


for _ in range(int(input())):
    n, m, lib, road = map(int, input().split())
    graph = dict()

    for _ in range(m):
        u, v = map(int, input().split())

        if u not in graph:
            graph[u] = list()

        if v not in graph:
            graph[v] = list()

        graph[u].append(v)
        graph[v].append(u)

    print(solve())
