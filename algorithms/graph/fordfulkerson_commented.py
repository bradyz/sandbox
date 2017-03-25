from collections import deque


# Macro.
INFINITY = float('inf')


def ford_fulkerson(graph, source, sink):
    """
    Finds the max flow from source to sink of a given graph.
    Does not modify the graph. Assumes that no node is labeled -1.

    Inputs:
        graph (dict<T, dict<T, int> >): undirected adjacency graph, where
                                        graph[u][v] = graph[v][u] = capacity.
        source (T): the start node.
        sink (T): the end node.
    Outputs:
        (int), the max flow through the graph.
    """
    def bfs(source, sink, capacity, previous):
        queue = deque()
        queue.appendleft(source)

        # Mark as visited.
        previous[source] = -1

        while len(queue) > 0:
            u = queue.popleft()

            # Go through edges and look for a potential path.
            for v in capacity.get(u, list()):
                if v in previous:
                    continue
                elif capacity[u][v] <= 0:
                    continue

                # Not visited and the edge allows positive flow.
                queue.appendleft(v)
                previous[v] = u

        # Can find an augmenting path.
        return sink in previous

    max_flow = 0

    # Make a copy of the graph - how much capacity is left on each edge.
    capacity = {u: type(v)(v) for u, v in graph.items()}
    parent = dict()

    # While there exists an augmenting path from source to sink.
    while bfs(source, sink, capacity, parent):
        path_flow = INFINITY

        # Look for the bottleneck capacity on edges u->v.
        v = sink
        while v != source:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v])
            v = u

        # Push the flow through the path.
        v = sink
        while v != source:
            u = parent[v]
            capacity[u][v] -= path_flow
            capacity[v][u] += path_flow
            v = u

        # Update the answer.
        max_flow += path_flow

        # Remember to clear the visited set for the next iteration.
        parent = dict()

    # Populate how much flow went through each edge.
    flows = {u: dict() for u in graph}

    for u in capacity:
        for v in capacity[u]:
            max_left = max(capacity[u][v], capacity[v][u])
            min_left = min(capacity[u][v], capacity[v][u])
            flow = type(max_flow)((max_left - min_left) / 2.0)

            flows[u][v] = flow
            flows[v][u] = flow

    return max_flow, flows


if __name__ == '__main__':
    # Example run, initial edge capacities.
    #               1
    #        10   / | \     1
    #           /   |   \
    #         s    5|     t
    #           \   |   /
    #         1   \ | /    10
    #               2

    # Sample undirected graph.
    s = 'src'
    t = 'dst'
    edges = [(s, 1, 10), (s, 2, 1),
             (1, 2, 5),
             (1, t, 1), (2, t, 10)]

    # Construct the undirected graph.
    graph = dict()
    for u, v, w in edges:
        if u not in graph:
            graph[u] = dict()
        if v not in graph:
            graph[v] = dict()
        graph[u][v] = w
        graph[v][u] = w

    # Example run, amount of flow through each edge, total of 7.
    #               1
    #      6/10   / | \   1/1
    #           /   |   \
    #         s  5/5|     t
    #           \   |   /
    #       1/1   \ | /  6/10
    #               2
    max_flow, flows = ford_fulkerson(graph, s, t)

    # Show the final results.
    print('Max flow: %d' % max_flow)

    for u in sorted(flows, key=lambda x: str(x)):
        for v in sorted(flows[u], key=lambda x: str(x)):
            print('Edge: %s <-> %s\t\tFlow: %s.' % (u, v, flows[u][v]))
