from sys import maxsize as MAX_INT


def dfs(c):
    global x, vis
    if v[c] not in u:
        x = min(x, v[c])
    vis.add(c)
    for j in range(n):
        if g[c][j] == "1" and j not in vis:
            dfs(j)

n = int(input())
v = list(map(int, input().split()))
g = [list(input()) for _ in range(n)]
u = set()
r = [0 for _ in range(n)]
for i in range(n):
    x = MAX_INT
    vis = set()
    dfs(i)
    r[i] = x
    u.add(x)
print(" ".join(list(map(str, r))))
