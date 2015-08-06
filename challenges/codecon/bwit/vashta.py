n = int(input())
m = int(input())
g = [list(map(int, input().split())) for _ in range(n)]
x = int(input())

for _ in range(x):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    mx, my = 0, 0
    for i in range(n):
        for j in range(m):
            if i in range(x1, x2) and j in range(y1, y2):
                continue
            if g[i][j] > g[mx][my]:
                mx, my = i, j
    print(str(mx) + " " + str(my))
