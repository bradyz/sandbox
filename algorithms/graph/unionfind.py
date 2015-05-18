class edge:
    def __init__(self, a, b, w):
        self.a = a      # to
        self.b = b      # from
        self.w = w      # weight

    def __str__(self):
        return "A: "+str(self.a)+" B: "+str(self.b)+" W: "+str(self.w)

    # used for plotting
    def tuple_rep(self):
        return ((self.a.x, self.a.y), (self.b.x, self.b.y))

    def to(self, fro):
        if fro == self.a.v:
            return self.b
        elif fro == self.b.v:
            return self.a
        else:
            return None


class point:
    def __init__(self, v, x, y):
        self.v = v      # point id
        self.x = x      # x coordinate
        self.y = y      # y coordinate

    def __str__(self):
        return str(self.v)


# O(n) complexity, depends on find
def union(p, x, y):
    p[find(p, x)] = find(p, y)      # join subsets


# O(n) complexity, has to go through at most all nodes
def find(p, i):
    if(p[i] == -1):
        return i
    return find(p, p[i])


def has_cycle(g, p):
    for e in g:
        # find the two subsets the nodes belong to
        x = find(p, e._a)
        y = find(p, e._b)

        # if the two points belong to the same subset
        if x == y:
            return True
        else:
            union(p, x, y)
            # p[x] = y equivalently, since x and y are parents

    return False

if __name__ == "__main__":
    # graph vis
    # 0
    # | \
    # 1 - 2
    edge_1 = edge(0, 1)
    edge_2 = edge(1, 2)
    edge_3 = edge(0, 2)

    # adjacency graph
    graph = [edge_1, edge_2, edge_3]
    n = len(graph)

    # initialize all parents to -1
    parents = [-1 for _ in range(n)]

    print(has_cycle(graph, parents))
