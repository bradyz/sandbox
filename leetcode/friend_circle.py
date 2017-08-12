def dfs(u, graph, visited):
    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            dfs(v, graph, visited)


class Solution(object):
    def findCircleNum(self, M):
        n = len(M)
        graph = {u: set() for u in range(n)}

        for i in range(n):
            for j in range(i+1):
                if M[i][j]:
                    graph[i].add(j)
                    graph[j].add(i)

        result = 0
        visited = set()

        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(i, graph, visited)
                result += 1

        return result
