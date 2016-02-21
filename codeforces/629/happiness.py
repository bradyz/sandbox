n = int(input())
g = [list(input()) for _ in range(n)]

ret = 0

for i in range(n):
    for j in range(n):
        if g[i][j] != "C":
            continue
        for x in range(j+1, n):
            ret += g[i][x] == "C"
        for y in range(i+1, n):
            ret += g[y][j] == "C"

print(ret)
