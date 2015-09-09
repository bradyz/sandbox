import sys

n = 0
c = []

for i, line in enumerate(sys.stdin):
    if i == 0:
        n = int(line)
    else:
        c.append(list(map(int, line.split(","))))

r = []
p = set()
points = 0

while n > 0 and c:
    c = list(sorted(c, key=lambda x: -x[1]/x[2]))
    for i in range(len(c)):
        if c[i] not in r:
            if c[i][2] > n:
                p.add(c[i][0])
            points += min(n, c[i][2]) * c[i][1] // c[i][2]
            n -= min(n, c[i][2])
            r.append(c[i][0])
            if n == 0:
                break

print(points)

arr = []

for v in sorted(r):
    res = str(v)
    if v in p:
        res += "*"
    arr.append(res)

print(",".join(map(str, arr)))
