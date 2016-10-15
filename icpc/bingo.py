from itertools import combinations


def solve(gs, have):
    grid = [["O" for _ in range(5)] for _ in range(5)]
    for g in gs:
        for i in range(5):
            for j in range(5):
                if g[i][j] == "X":
                    grid[i][j] = "X"
    need = [0 for _ in range(5)]
    for j in range(5):
        for i in range(5):
            need[j] += (grid[i][j] == "X" and not (i == 2 and j == 2))
    result = 0
    for h, n in zip(have, need):
        result += max(n - h, 0)
    return result


for _ in range(int(input())):
    line = list(map(int, input().split()))
    have = line[:-2]
    x = line[-2]
    y = line[-1]
    grids = [list() for _ in range(x)]
    for _ in range(5):
        for i, grid in enumerate(input().split()):
            grids[i].append(grid)
    r = 25
    for grid_subset in combinations(grids, y):
        r = min(r, solve(grid_subset, have))
    print(r)
