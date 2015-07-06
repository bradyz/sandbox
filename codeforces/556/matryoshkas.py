n, m = map(int, input().split())
c = {}
r = 0
for _ in range(m):
    t = list(map(int, input().split()))
    c[t[1]] = t[2:]
d = list(c.keys())
for v in d:
    while c[v] and c[v] != list(range(v+1, c[v][-1]+1)):
        r += 1
        c[c[v].pop()] = []
print(r + len(c.keys()) - 1)
