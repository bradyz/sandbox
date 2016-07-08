class Solution(object):
    def findMinHeightTrees(self, n, edges):
        g = {u: set() for u in range(n)}
        z = set(range(n))
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            if len(g[u]) > 1 and u in z:
                z.remove(u)
            if len(g[v]) > 1 and v in z:
                z.remove(v)
        last = set()
        while z:
            last = set(z)
            x = set()
            for u in z:
                for v in g[u]:
                    g[v].remove(u)
                    if len(g[v]) == 1:
                        x.add(v)
            z = x
        return list(last)


s = Solution()
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(s.findMinHeightTrees(n, edges))
