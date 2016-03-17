n, r, c = map(int, input().split())
g = [[0 for _ in range(c)] for _ in range(r)]
ret = n
for i in range(r):
    for j in range(c):
        if ret == 0:
            continue
        elif i > 0 and g[i-1][j] != 0 and (g[i-1][j] % 2) == (ret % 2):
            continue
        elif j > 0 and g[i][j-1] != 0 and (g[i][j-1] % 2) == (ret % 2):
            continue
        g[i][j] = ret
        ret -= 1
if ret == 0:
    for l in g:
        print(" ".join(map(str, l)))
else:
    print(-1)
