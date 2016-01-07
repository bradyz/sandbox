H, W = map(int, input().split())
grid = ["|" * (W+1)] + ["|" + input() for _ in range(H)]
Q = int(input())

hor = [[0 for _ in range(W+1)] for _ in range(H+1)]
ver = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(1, H+1):
    for j in range(1, W+1):
        hor[i][j] = hor[i-1][j] + hor[i][j-1] - hor[i-1][j-1]
        ver[i][j] = ver[i-1][j] + ver[i][j-1] - ver[i-1][j-1]
        if grid[i][j-1] == "." and grid[i][j] == ".":
            hor[i][j] += 1
        if grid[i-1][j] == "." and grid[i][j] == ".":
            ver[i][j] += 1

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    answer = 0
    answer += ver[r2][c2] - ver[r1][c2] - ver[r2][c1-1] + ver[r1][c1-1]
    answer += hor[r2][c2] - hor[r2][c1] - hor[r1-1][c2] + hor[r1-1][c1]

    print(answer)
