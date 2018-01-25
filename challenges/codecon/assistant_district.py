N = 51

grid = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    grid[x][y] = 1

for i in range(1, N):
    grid[i][0] += grid[i-1][0]
    grid[0][i] += grid[0][i-1]

for i in range(1, N):
    for j in range(1, N):
        grid[i][j] += max(grid[i-1][j], grid[i][j-1])

print(grid[N-1][N-1])
