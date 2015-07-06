n, m = map(int, input().split())
c = {}
r = 0

for _ in range(m):
    t = list(map(int, input().split()))
    c[t[1]] = t[2:]

d = list(c.keys())

for v in d:
    if v == 1:
        if c[v]:
            x = 0
            for i in range(len(c[v])):
                if c[v][i] != i + 2:
                    break
                x += 1
            r += len(c[v]) - x
    else:
        r += len(c[v])

print(len(d) + r * 2 - 1)
