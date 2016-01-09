DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(orig, x, y, dx, dy):
    left[orig].add((x, y))
    if x + dx < 0 or x + dx >= 2 or y + dy < 0 or y + dy >= N or grid[x+dx][y+dy] == "X":
        return
    dfs(orig, x + dx, y + dy, dx, dy)


for T in range(int(input())):
    N = int(input())
    grid = [list(input()) for _ in range(2)]
    left = dict()

    for i in range(2):
        for j in range(N):
            if grid[i][j] == "X":
                continue
            cell = (i, j)
            left[cell] = set()
            for dx, dy in DIR:
                dfs(cell, cell[0], cell[1], dx, dy)

    result = 0

    while left:
        least_cell = min(left, key=lambda x: len(left[x]))
        best_cell = max(left[least_cell], key=lambda x: len(left[x]))
        to_pop = set([best_cell, least_cell])

        for cell in left[best_cell]:
            if cell in to_pop:
                continue
            to_pop.add(cell)
            for another in left[cell]:
                if another in to_pop:
                    continue
                left[another].remove(cell)
                if not left[another]:
                    to_pop.add(another)

        for cell in left[least_cell]:
            if cell == least_cell:
                continue
            left[cell].remove(least_cell)
            if not left[cell]:
                to_pop.add(cell)

        for cell in to_pop:
            if cell in left:
                left.pop(cell)

        result += 1

    print("Case #" + str(T+1) + ": " + str(result))
