n, m = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(n)]
x, y = map(int, input().split())
d = [list(map(int, input().split())) for _ in range(x)]
r = 0
g = [[0 for j in range(m + 2 * (y-1))] for i in range(n + 2 * (x-1))]
for i in range(n):
    for j in range(m):
        g[i+x-1][j+y-1] = c[i][j]
for a in range(n+2*(x-1)-x+1):
    for b in range(m+2*(y-1)-y+1):
        t = [[0 for j in range(m + 2 * (y-1))] for i in range(n + 2 * (x-1))]
        for i in range(x):
            for j in range(y):
                t[i+a][j+b] = d[i][j]
        cont = True
        i = 0
        j = 0
        gamma = 0
        while cont and i < n + 2 * (x-1):
            while cont and j < m + 2 * (y-1):
                if g[i][j] == t[i][j] or t[i][j] == 0 or g[i][j] == 0:
                    if g[i][j] == t[i][j]:
                        gamma += t[i][j]
                else:
                    cont = False
                    break
                j += 1
            i += 1
            j = 0
        r = max(r, gamma)
print(r)
