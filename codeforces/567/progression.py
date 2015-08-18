from math import factorial

n, k = map(int, input().split())
d = {}
r = 0

for v in map(int, input().split()):
    if v in d:
        d[v] += 1
    else:
        d[v] = 1

if k == 1:
    def choose(m, l):
        return factorial(m) // factorial(l) // factorial(m-l)

    for v in d:
        if d[v] >= 3:
            r += choose(d[v], 3)
else:
    for v in d:
        t1 = v / k
        t2 = v / k / k
        if t1 in d and t2 in d:
            r += d[t1] * d[t2] * d[v]

print(r)
