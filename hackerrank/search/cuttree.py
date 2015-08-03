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


def dfsV2(u):
    s = [u]
    vis = set()

    while s:
        t = s[-1]
        vis.add(t)
        m = False

        for v in d[t]:
            if v not in vis:
                s.append(v)
                m = True

        if not m:
            tmp = c[t-1]
            for v in d[t]:
                if v in w:
                    tmp += w[v]
            w[t] = tmp
            s.pop()


w = dict()
dfsV2(list(d.keys())[0])

root = max(w.values())
r = sys.maxsize

for u in w:
    if w[u] != root:
        r = min(r, abs(root-2*w[u]))

print(r)
