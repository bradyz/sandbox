import sys

n = int(input())
c = list(map(int, input().split()))
d = dict()

for line in sys.stdin:
    u, v = map(int, line.split())
    if u in d:
        d[u].append(v)
    else:
        d[u] = [v]

    if v in d:
        d[v].append(u)
    else:
        d[v] = [u]


def dfs(u, vis):
    vis.add(u)

    if u not in d:
        return c[u-1]
    elif u in w:
        return w[u]

    t = c[u-1]

    for v in d[u]:
        if v not in vis:
            vis_c = type(vis)(vis)
            t += dfs(v, vis_c)

    w[u] = t

    return t

w = dict()

for node in d:
    vis_i = set()
    dfs(node, vis_i)

root = max(w.values())
r = sys.maxsize

for u in w:
    if w[u] != root:
        r = min(r, abs(root-2*w[u]))

print(r)
