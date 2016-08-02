n = int(input())
c = list(map(int, input().split()))
p = list()
for i in range(1, int(1e9)):
    if 2 ** i > int(1e9) * 2:
        break
    p.append(2 ** i)
v = dict()
d = dict()
for x in c:
    for y in p:
        if 2 * x == y:
            d[x] = d.get(x, 0) + 1
            continue
        v[y - x] = v.get(y - x, 0) + 1
r = 0
for x in c:
    r += v.get(x, 0)
for x in d.values():
    r += (x * (x - 1))
print(r // 2)
