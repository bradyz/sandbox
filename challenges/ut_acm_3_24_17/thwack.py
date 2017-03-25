def solve(grid, m, n, h):
    sx, sy = None, None
    ex, ey = None, None
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "A":
                sx, sy = i, j
            if grid[i][j] == "W":
                ex, ey = i, j

    go = [(sx, sy)]
    visited = set([sx, sy])

    while go:
        x, y = go.pop()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif (nx, ny) in visited:
                continue
            elif grid[nx][ny] != "W" and grid[nx][ny] != "A":
                height = int(grid[nx][ny])
                if height != -1 and h >= height:
                    continue

            visited.add((nx, ny))
            go.append((nx, ny))

    if (ex, ey) in visited:
        return "LUNCH!"
    return "THWACK!"


for _ in range(int(input())):
    m, n = map(int, input().split())
    h = int(input())
    grid = [input().split() for _ in range(m)]

    print(solve(grid, m, n, h))
