import numpy as np
import matplotlib.pyplot as plt


class edge:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def __str__(self):
        return str(self._a) + " " + str(self._b)


def union(p, x, y):
    x_p = find(p, x)
    y_p = find(p, y)
    p[x_p] = y_p


def find(p, i):
    if(p[i] == -1):
        return i
    return find(p, p[i])


def has_cycle(g, p):
    for e in g:
        x = find(p, e._a)
        y = find(p, e._b)

        if x == y:
            return True
        else:
            union(p, x, y)

    return False

if __name__ == "__main__":
    n = 3

    edge_1 = edge(0, 1)
    edge_2 = edge(1, 2)
    edge_3 = edge(0, 2)

    graph = [edge_1, edge_3, edge_2]

    parents = [-1 for _ in range(n)]

    print(has_cycle(graph, parents))
