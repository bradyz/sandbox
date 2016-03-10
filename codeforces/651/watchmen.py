c = [tuple(map(int, input().split())) for _ in range(int(input()))]
o = dict()
x = dict()
y = dict()
for v in c:
    o[v] = o.get(v, 0) + 1
    x[v[0]] = x.get(v[0], 0) + 1
    y[v[1]] = y.get(v[1], 0) + 1
ret = 0
for v in x:
    ret += (x[v] * (x[v] - 1)) // 2
for v in y:
    ret += (y[v] * (y[v] - 1)) // 2
for v in o:
    ret -= (o[v] * (o[v] - 1)) // 2
print(ret)
