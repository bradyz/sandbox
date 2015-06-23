from math import sqrt
n = int(input())
c = {}
d = {}
m = set()

for _ in range(n):
    t = input().split(',')
    c[t[-1]] = list(map(int, t[:3])) + [t[-2]]

for u in c:
    for v in c:
        if u == v:
            continue
        if sqrt((c[u][0]-c[v][0])**2+(c[u][1]-c[v][1])**2+(c[u][2]-c[v][2])**2) < float(c[u][-1]):
            if u not in d:
                d[u] = [v]
            else:
                d[u].append(v)


def dfs(u, vis):
    global d
    vis.add(u)
    if u not in d:
        return

    for v in d[u]:
        if v not in vis:
            dfs(v, vis)

for u in d:
    t = set()
    dfs(u, t)
    if len(t) > len(m):
        m = t

print(",".join(sorted(list(m))))
