DIR = [(-1, 0), (1, 0), (0, 1), (0, -1)]


def dfs(i, j):
    component = list()
    stack = [(i, j)]
    vis[i][j] = True
    while stack:
        x, y = stack.pop()
        component.append((x, y))
        for dx, dy in DIR:
            xp, yp = x + dx, y + dy
            if xp < 0 or yp < 0 or xp >= n or yp >= m:
                continue
            elif vis[xp][yp]:
                continue
            elif grid[xp][yp] == "*":
                continue
            vis[xp][yp] = True
            stack.append((xp, yp))
    for x, y in component:
        size[x][y] = len(component)
        parent[x][y] = (i, j)

n, m = map(int, input().split())
grid = [input() for _ in range(n)]
vis = [[False for _ in range(m)] for _ in range(n)]
size = [[0 for _ in range(m)] for _ in range(n)]
parent = {i: dict() for i in range(n)}
for i in range(n):
    for j in range(m):
        if vis[i][j]:
            continue
        elif grid[i][j] == "*":
            continue
        dfs(i, j)
for x in range(n):
    res = list()
    for y in range(m):
        if grid[x][y] == "*":
            tmp = 1
            seen = set()
            for dx, dy in DIR:
                xp, yp = x + dx, y + dy
                if xp < 0 or yp < 0 or xp >= n or yp >= m:
                    continue
                elif grid[xp][yp] == "*":
                    continue
                elif parent[xp][yp] in seen:
                    continue
                seen.add(parent[xp][yp])
                tmp += size[xp][yp]
            res.append(tmp % 10)
        else:
            res.append(grid[x][y])
    print("".join(map(str, res)))
