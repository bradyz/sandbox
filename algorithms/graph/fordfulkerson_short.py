from collections import deque


def ford_fulkerson(graph, s, t):
    def bfs():
        queue = deque([s])
        for u in list(prev.keys()):
            prev.pop(u)
        prev[s] = None
        while len(queue) > 0:
            u = queue.popleft()
            for v in graph.get(u, dict()):
                if v not in prev and graph[u][v] > 0:
                    queue.appendleft(v)
                    prev[v] = u
        return t in prev

    max_flow = 0
    prev = dict()
    while bfs():
        flow = float('inf')
        v = t
        while v != s:
            flow = min(flow, graph[prev[v]][v])
            v = prev[v]
        v = t
        while v != s:
            graph[prev[v]][v] -= flow
            graph[v][prev[v]] += flow
            v = prev[v]
        max_flow += flow

    return max_flow
