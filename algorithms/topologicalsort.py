def topological_sort(g):
    def topological_util(u):
        vis.add(u)

        if u in g:
            for v in g[u]:
                if v not in vis:
                    topological_util(v)

        s.append(u)

    s = []
    vis = set()

    for node in g:
        if node not in vis:
            topological_util(node)

    return list(reversed(s))


if __name__ == "__main__":
    num_nodes = int(input())
    graph = {}

    # construct adjacency list
    for _ in range(num_nodes):
        u, v = map(int, input().split())
        if u not in graph:
            graph[u] = [v]
        else:
            graph[u].append(v)

    print(topological_sort(graph))
