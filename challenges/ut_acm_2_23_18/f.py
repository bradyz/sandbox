from collections import defaultdict


def dfs(graph, start, visited, color):
    if start in visited:
        return False

    stack = [start]

    while stack:
        vertex = stack.pop()
        visited.add(vertex)

        if color[vertex] == 1:
            return True

        color[vertex] = 1

        stack.extend((graph[vertex]))

        if not graph[vertex]:
            color[vertex] = 2

    return False


def cycle_exists(graph):
    color = {i: 0 for i in range(n)}
    visited = set()


    for vertex in list(graph.keys()):
        if dfs(graph, vertex, visited, color):
            return True

    return False


for _ in range(int(input())):
    n, m = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(m):
        u, v = map(int, input().split())

        graph[u].append(v)

    if cycle_exists(graph):
        print('TOO SMALL')
    else:
        print('TOO BIG')
