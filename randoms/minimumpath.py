# www.geeksforgeeks.org/collect-maximum-points-in-a-grid-using-two-traversals
# Collect maximum points in a grid using two traversals (Dynamic Programming)

from sys import maxsize as INF


# O(NM) time, O(NM) space
def max_path(g, n, m):
    r = [[INF for j in range(m)] for i in range(n)]

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                r[i][j] = g[i][j]

            if i > 0:
                r[i][j] = min(r[i][j], r[i-1][j] + g[i][j])
            if j > 0:
                r[i][j] = min(r[i][j], r[i][j-1] + g[i][j])
            if i > 0 and j > 0:
                r[i][j] = min(r[i][j], r[i-1][j-1] + g[i][j])

    # from pprint import PrettyPrinter
    # pp = PrettyPrinter()
    # pp.pprint(r)

    return r[n-1][m-1]

if __name__ == "__main__":
    rows, cols = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(rows)]
    print(max_path(grid, rows, cols))
