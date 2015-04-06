from copy import copy


class Graph:
    def __init__(self, num):
        self.edges = [[] for _ in range(num)]
        self.nodes = set()

    def add_edge(self, a, b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.edges.append((a, b))

    def dfs(self, vis=None, cur=-1):
        if not vis:
            vis = [False for _ in self.nodes]
            for i in range(len(self.edges)):
                for j in range(len(self.edges[i])):
                    if not vis[self.edges[i][j]]:
                        print("New Start: " + str(self.edges[i][j]))
                        a = copy(vis)
                        a[self.edges[i][j]] = True
                        self.dfs(a, self.edges[i][j])
        else:
            for j in range(len(self.edges[cur])):
                if not vis[self.edges[cur][j]]:
                    print(self.edges[cur][j])
                    a = copy(vis)
                    a[self.edges[cur][j]] = True
                    self.dfs(a, self.edges[cur][j])


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.dfs()
