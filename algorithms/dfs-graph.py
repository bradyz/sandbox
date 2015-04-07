from copy import copy


class Graph:
    def __init__(self, num):
        self.edges = [[] for _ in range(num)]
        self.nodes = set()

    def add_edge(self, a, b):
        self.nodes.add(a)
        self.nodes.add(b)
        self.edges[a].append(b)

    def dfs(self, vis=None, cur=-1, path=None):
        if not vis:
            vis = set()
            for i in range(len(self.edges)):
                if i not in vis:
                    vis.add(i)
                    self.dfs(set([i]), i, [i])
        else:
            for j in range(len(self.edges[cur])):
                if self.edges[cur][j] not in vis:
                    vis.add(self.edges[cur][j])
                    self.dfs(vis, self.edges[cur][j], path+[self.edges[cur][j]])
            if len(set(self.edges[cur])-vis) == 0:
                print(path)


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.dfs(cur=2)
