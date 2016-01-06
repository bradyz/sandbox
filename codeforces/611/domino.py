H, W = map(int, input().split())
grid = [input() for _ in range(H)]
Q = int(input())

hor = [[0 for _ in range(W+1)] for _ in range(H+1)]
ver = [[0 for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
    for j in range(W):
        hor[i+1][j+1] = hor[i][j+1] + hor[i+1][j] - hor[i][j]
        ver[i+1][j+1] = ver[i][j+1] + ver[i+1][j] - ver[i][j]
        if grid[i][j] == "#":
            continue
        if j != W-1 and grid[i][j+1] == ".":
            hor[i+1][j+1] += 1
        if i != H-1 and grid[i+1][j] == ".":
            ver[i+1][j+1] += 1

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())

    answer = 0
    answer += hor[r2-1][c2] - hor[r1][c2] - hor[r2-1][c1] + hor[r1][c1]
    answer += ver[r2][c2-1] - ver[r1][c2-1] - ver[r2][c1] + ver[r1][c1]

    print(answer)
