n = int(input())
v = list(map(int, input().split()))
g = [list(input()) for _ in range(n)]
u = [False for _ in range(n+1)]
r = [0 for _ in range(n)]
w = [-1 for _ in range(n+1)]
s = []
for i in range(n):
    x = n
    s.append(i)
    while s:
        c = s.pop()
        if not u[v[c]]:
            x = min(x, v[c])
        w[c] = i
        for j in range(n):
            if g[c][j] == "1" and w[j] != i:
                s.append(j)
    r[i] = x
    u[x] = True
print(" ".join(list(map(str, r))))
