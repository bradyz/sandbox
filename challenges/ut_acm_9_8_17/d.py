def dfs(u, d, graph, visited):
    if u == d:
        return

    for v in graph.get(u, list()):
        if v in visited:
            continue

        visited.add(v)
        dfs(v, d, graph, visited)


for _ in range(int(input())):
    s, d = input().split()

    graph = dict()

    for _ in range(int(input())):
        u, v = input().split()

        if u not in graph:
            graph[u] = list()

        graph[u].append(v)

    visited = set()
    dfs(s, d, graph, visited)

    if d in visited:
        print('Yes')
    else:
        print('No')
