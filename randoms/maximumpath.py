# Collect maximum points in a grid using two traversals (Dynamic Programming)
# http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

from sys import maxsize as INF


# O(NM) time, O(NM) space
def max_path(g, n, m):
    r = [[-INF for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                r[i][j] = g[i][j]

            if i > 0:
                r[i][j] = max(r[i][j], r[i-1][j] + g[i][j])
            if j > 0:
                r[i][j] = max(r[i][j], r[i][j-1] + g[i][j])
            if i > 0 and j > 0:
                r[i][j] = max(r[i][j], r[i-1][j-1] + g[i][j])

    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    pp.pprint(r)

    return r[n-1][m-1]


# O(2^mn) time, O(1) space
def max_pathV2(g, n, m):
    def dfs(x, y):
        if x < 0 or y < 0 or x >= n or y >= m:
            return -INF

        if x == n-1 and y == m-1:
            return g[x][y]

        return(max(dfs(x+1, y), dfs(x, y+1)) + g[x][y])

    return dfs(0, 0)

if __name__ == "__main__":
    rows, cols = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    print(max_path(grid, rows, cols))
    print(max_pathV2(grid, rows, cols))
