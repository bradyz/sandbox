def spread(x, y, grid, m, n):
    que = [(x, y)]
    visited = set([(x, y)])
    while que:
        x, y = que.pop()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif grid[ny][nx] == "X" or (nx, ny) in visited:
                continue
            if grid[ny][nx] == "A":
                grid[ny][nx] = "B"
            elif grid[ny][nx] == "B":
                grid[ny][nx] = "C"
            elif grid[ny][nx] == "C":
                grid[ny][nx] = "D"
            elif grid[ny][nx] == "D":
                visited.add((nx, ny))
                que.append((nx, ny))


def pulse(x, y, grid, m, n):
    if grid[y][x] == "A":
        grid[y][x] = "B"
    elif grid[y][x] == "B":
        grid[y][x] = "C"
    elif grid[y][x] == "C":
        grid[y][x] = "D"
    elif grid[y][x] == "D":
        spread(x, y, grid, m, n)


def solve(grid, outbreaks, m, n):
    for x, y in outbreaks:
        pulse(x, y, grid, m, n)
    for row in grid:
        print("".join(map(str, row)))


for _ in range(int(input())):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(m)]
    outbreaks = [list(map(int, input().split())) for _ in range(int(input()))]
    solve(grid, outbreaks, m, n)
