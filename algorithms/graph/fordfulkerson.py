from queue import Queue
from copy import deepcopy
from sys import maxsize


def ford_fulkerson(a_graph, s, t):
    # typical bfs
    def bfs():
        q = Queue()
        vis = set()
        q.put(s)
        vis.add(s)
        parent[s] = -1

        while not q.empty():
            cur = q.get()

            for i in range(len(r_graph)):
                if i not in vis and r_graph[cur][i] > 0:
                    q.put(i)
                    vis.add(i)
                    parent[i] = cur                 # create the path

        return t in vis                             # can reach the sink

    r_graph = deepcopy(a_graph)                     # residual capacity graph
    parent = [0 for _ in range(len(r_graph))]       # trace of path for bfs
    max_flow = 0

    # while there exists an augmenting path
    while(bfs()):
        path_flow = maxsize
        v = t
        # look for the bottleneck capacity
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, r_graph[u][v])
            v = parent[v]

        v = t
        # update the residual graph
        while v != s:
            u = parent[v]
            r_graph[u][v] -= path_flow
            r_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    # use to see the residual graph, the actual flows through edges
    from pprint import PrettyPrinter
    pp = PrettyPrinter()

    pp.pprint(r_graph)
    print(max_flow)

if __name__ == "__main__":
    # adjacency graph
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    # source of 0, sink of 5
    ford_fulkerson(graph, 0, 5)
