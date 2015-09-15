from queue import PriorityQueue
from sys import maxsize as MAXINT


class Node:
    def __init__(self, v):
        self.v = v

    def __lt__(self, rhs):
        dist_self = (self.v in d and d[self.v]) or MAXINT
        dist_rhs = (rhs.v in d and d[rhs.v]) or MAXINT
        return dist_self < dist_rhs

    def __eq__(self, rhs):
        dist_self = (self.v in d and d[self.v]) or MAXINT
        dist_rhs = (rhs.v in d and d[rhs.v]) or MAXINT
        return dist_self == dist_rhs


def path(u):
    v = u
    r = []
    while v != -1:
        r.append(v)
        v = p[v]
    return " ".join(map(str, reversed(r)))


def dijkstra():
    q = PriorityQueue()
    q.put(Node(1))
    d[1] = 0
    while not q.empty():
        u = q.get().v
        if u == n:
            return path(u)
        for v in g[u]:
            if v not in d or d[v] > d[u] + g[u][v]:
                d[v] = d[u] + g[u][v]
                p[v] = u
                q.put(Node(v))
    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = {i: {} for i in range(1, n+1)}
    d = {}
    p = {1: -1}

    for _ in range(m):
        u, v, w = map(int, input().split())
        if v not in g[u] or u not in g[v]:
            g[u][v] = w
            g[v][u] = w
        else:
            g[u][v] = min(g[u][v], w)
            g[v][u] = min(g[u][v], w)

    print(dijkstra())
