from collections import deque


DIR = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def bfs(sx, sy, ex, ey, grid):
    q = deque()
    v = set([(sx, sy)])

    q.appendleft((sx, sy, 0))

    while q:
        x, y, d = q.pop()

        if x == ex and y == ey:
            return d

        for dx, dy in DIR:
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif (nx, ny) in v:
                continue
            elif not grid[nx][ny]:
                continue

            v.add((nx, ny))
            q.appendleft((nx, ny, d + 1))




n = int(input())
grid = [input() for _ in range(n)]
can = [[True for _ in range(n)] for _ in range(n)]
sx, sy = None, None

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'M':
            sx, sy = i, j
        if grid[i][j] == 'T':
            ex, ey = i, j

        for x in range(n):
            for y in range(n):
                if grid[i][j] == 'M' or grid[i][j] == 'T':
                    continue
                if grid[x][y] == 'M' or grid[x][y] == 'T':
                    continue
                if grid[i][j] != 'O':
                    continue
                if grid[x][y] == 'O':
                    continue

                shoot = int(grid[x][y])

                if (i - x) ** 2 + (j - y) ** 2 < shoot ** 2:
                    can[i][j] = False

                can[x][y] = False

print(bfs(sx, sy, ex, ey, can))
