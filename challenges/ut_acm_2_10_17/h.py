for _ in range(int(input())):
    n, m = map(int, input().split())

    graph_reversed = {u: set() for u in range(1, n+1)}
    graph = {u: set() for u in range(1, n+1)}
    graph_copy = {u: set() for u in range(1, n+1)}
    last = {u for u in range(1, n+1)}

    for _ in range(m):
        u, v = map(int, input().split())
        graph_reversed[v].add(u)
        graph[u].add(v)
        graph_copy[u].add(v)
        if u in last:
            last.remove(u)

    cost = dict()
    next_last = set()
    for u in last:
        cost[u] = 0.0
        for v in graph_reversed[u]:
            graph_copy[v].remove(u)
            if not graph_copy[v]:
                next_last.add(v)
    last = next_last

    while last:
        next_last = set()
        for u in last:
            result = 0.0
            for v in graph[u]:
                result += cost[v]
            result = result / len(graph[u]) + 1.0
            cost[u] = result

            for v in graph_reversed[u]:
                graph_copy[v].remove(u)
                if not graph_copy[v]:
                    next_last.add(v)
        last = next_last

    print("%.3f" % cost[1])
