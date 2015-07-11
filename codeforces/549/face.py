n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
r = 0

for i in range(n-1):
    for j in range(m-1):
        if set([g[i][j], g[i+1][j+1], g[i][j+1], g[i+1][j]]) == set('face'):
            r += 1

print(r)
