from queue import Queue


def max_flow(graph, sources, t):
    def bfs():
        q = Queue()
        vis = set()

        for s in sources:
            q.put(s)
            vis.add(s)
            parent[s] = -1

        while not q.empty():
            u = q.get()

            for v in graph.get(u, []):
                if v not in vis and graph[u][v] > 0:
                    q.put(v)
                    vis.add(v)
                    parent[v] = u

        return t in vis

    parent = dict()
    max_flow = 0

    while bfs():
        path_flow = float("inf")
        v = t

        while v not in sources:
            u = parent[v]
            path_flow = min(path_flow, graph[u][v])
            v = parent[v]

        v = t
        while v not in sources:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    return max_flow


if __name__ == "__main__":
    n, m, k, q = map(int, input().split())
    graph = dict()

    for _ in range(m):
        u, v, w = map(int, input().split())
        if u not in graph:
            graph[u] = dict()
        if v not in graph:
            graph[v] = dict()
        graph[u][v] = w
        graph[v][u] = w

    sources = set(map(int, input().split()))

    print(max_flow(graph, sources, q))
