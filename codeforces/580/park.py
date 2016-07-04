n, m = map(int, input().split())
c = [0] + list(map(int, input().split()))
g = {i: list() for i in range(1, n+1)}
for _ in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
r = 0
vis = set([1])
s = [(1, c[1])]
while s:
    u, w = s.pop()
    if w > m:
        continue
    found = False
    for v in g[u]:
        if v in vis:
            continue
        vis.add(v)
        found = True
        if c[v] == 0:
            s.append((v, 0))
        else:
            s.append((v, w + c[v]))
    if not found:
        r += 1
print(r)
