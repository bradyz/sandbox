def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= n or (i, j) in s or g[i][j] == 0:
        return 0
    s.add((i, j))
    for x, y in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        dfs(i+x, j+y)
    return 1

for _ in range(int(input())):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(n)]
    s = set()
    print(sum(dfs(i, j) for i in range(n) for j in range(n)))
