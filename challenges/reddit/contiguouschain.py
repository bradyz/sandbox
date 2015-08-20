def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m or v[x][y] or g[x][y] != "x":
        return 0

    v[x][y] = True

    dfs(x+1, y)
    dfs(x-1, y)
    dfs(x, y+1)
    dfs(x, y-1)

    return 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    v = [[False for j in range(m)] for i in range(n)]
    r = 0

    for i in range(n):
        for j in range(m):
            r += dfs(i, j)

    print(r)
