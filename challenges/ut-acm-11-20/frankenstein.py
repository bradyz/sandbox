import sys

def dfs(u):
    tmp.append(u)
    if u not in g:
        return
    for v in g[u]:
        if v in vis:
            continue
        vis.add(v)
        dfs(v)

g = {}

for line in sys.stdin:
    u, v = line.split()
    if u not in g:
        g[u] = [v]
    else:
        g[u].append(v)
    if v not in g:
        g[v] = [u]
    else:
        g[v].append(u)

total = list()
vis = set()
for u in g:
    if u in vis:
        continue
    vis.add(u)
    tmp = list()
    dfs(u)
    total.append(tmp)

best = max(total, key=len)
print(" ".join(sorted(best)))
