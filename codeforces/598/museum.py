def dfs(x, y):
    vis[x][y] = True
    path.append((x, y))
    paintings = 0
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        x1, y1 = x+dx, y+dy
        if x1 < 0 or x1 >= n or y1 < 0 or y1 >= m or vis[x1][y1]:
            continue
        if grid[x1][y1] == "*":
            paintings += 1
        else:
            vis[x1][y1] = True
            paintings += dfs(x1, y1)
    return paintings

if __name__ == "__main__":
    n, m, k = map(int, input().split())
    grid = [input() for _ in range(n)]
    count = [[0 for _ in range(m)] for _ in range(n)]
    vis = [[False for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] != "*":
                path = list()
                paintings = dfs(i, j)
                for x, y in path:
                    count[x][y] = paintings

    for _ in range(k):
        x, y = map(int, input().split())
        print(count[x-1][y-1])
