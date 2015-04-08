from copy import deepcopy
from pprint import PrettyPrinter


def brute_force(g, n, m, k):
    new_grid = []
    b = 2*k+1

    for i in range(n):
        new_row = []
        for j in range(m):
            av = 0
            for x in range(-k, k+1):
                for y in range(-k, k+1):
                    if i+x >= 0 and i+x < n and j+y >= 0 and j+y < m:
                        av += grid[i+x][j+y]
            av /= b*b
            new_row.append(round(av))
        new_grid.append(new_row)

    for row in new_grid:
        print(" ".join(map(str, row)))

    return

def summed_area(g, n, m, k):
    g1 = [[0 for _ in range(m)] for __ in range(n)]
    g2 = deepcopy(g1)

    for i in range(n):
        for j in range(m):
            g1[i][j] = g[i][j]
            if i > 0:
                g1[i][j] += g1[i-1][j]
            if j > 0:
                g1[i][j] += g1[i][j-1]
            if i > 0 and j > 0:
                g1[i][j] -= g1[i-1][j-1]

    # for row in g1:
    #     print(" ".join(map(str, row)))

    for i in range(n):
        for j in range(m):
            a = g1[max(0, i-k-1)][max(0, j-k-1)]
            b = g1[max(0, i-k-1)][min(m-1, j+k)]
            c = g1[min(n-1, i+k)][max(0, j-k-1)]
            d = g1[min(n-1, i+k)][min(m-1, j+k)]
            if i-k-1 < 0:
                a = 0
                b = 0
            if j-k-1 < 0:
                a = 0
                c = 0
            g2[i][j] = round((a+d-c-b) / (2*k+1)**2)

    for row in g2:
        print(" ".join(map(str, row)))


for _ in range(int(input())):
    args = [int(v) for v in input().split()]
    nA = args[0]
    mA = args[1]
    kA = args[2]
    grid = []

    for __ in range(nA):
        grid.append([int(v) for v in input().split()])

    brute_force(grid, nA, mA, kA)
    summed_area(grid, nA, mA, kA)
