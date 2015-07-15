import sys
from copy import copy

c = [tuple(map(str, line.strip().split("|"))) for line in sys.stdin]
v = {}

for i in range(len(c)):
    if c[i][0] in v:
        v[c[i][0]].append(c[i][1])
    else:
        v[c[i][0]] = [c[i][1]]

    if c[i][1] not in v:
        v[c[i][1]] = []

r = []

def dfs(key, t, vis):
    global v
    z = []
    m = []
    a = copy(vis)
    a.append(key)
    if len(v[key]) == 0:
        return a
    for y in v[key]:
        if y not in vis:
            z.append(dfs(y, t+1, a))
    for y in z:
        if len(y) > len(m):
            m = y
    return m

for x in v:
    l = list()
    m = dfs(x, 0, l)
    if len(m) > len(r):
        r = m

print("\n".join(r))
