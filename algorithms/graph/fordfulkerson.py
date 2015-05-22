from queue import Queue
from copy import deepcopy
from sys import maxsize


def ford_fulkerson(a_graph, s, t):
    def bfs():
        q = Queue()
        v = set()
        q.put(s)
        v.add(s)
        parent[s] = -1

        while not q.empty():
            cur = q.get()

            for i in range(len(r_graph)):
                if i not in v and r_graph[cur][i] > 0:
                    q.put(i)
                    v.add(i)
                    parent[i] = cur

        return t in v

    r_graph = deepcopy(graph)
    parent = [0 for _ in range(len(r_graph))]
    max_flow = 0

    while(bfs()):
        path_flow = maxsize
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, r_graph[u][v])
            v = parent[v]

        v = t
        while v != s:
            u = parent[v]
            r_graph[u][v] -= path_flow
            r_graph[v][u] += path_flow
            v = parent[v]

        max_flow += path_flow

    from pprint import PrettyPrinter
    pp = PrettyPrinter()

    pp.pprint(r_graph)
    print(max_flow)

if __name__ == "__main__":
    graph = [[0, 16, 13, 0, 0, 0],
             [0, 0, 10, 12, 0, 0],
             [0, 4, 0, 0, 14, 0],
             [0, 0, 9, 0, 0, 20],
             [0, 0, 0, 7, 0, 4],
             [0, 0, 0, 0, 0, 0]]

    ford_fulkerson(graph, 0, 5)
