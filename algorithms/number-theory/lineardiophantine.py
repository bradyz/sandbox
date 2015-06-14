v = {}


def solve(a, b):
    if a < b:
        a, b = b, a
    x = a % b
    if x == 0:
        return
    y = (a - x) * -1 // b
    v[x] = [(1, a), (y, b)]
    solve(x, b)


def flatten(c):
    global x, y
    t = {x: 0, y: 0}
    for i in range(len(c)):
        co = c[i][0]
        if type(c[i][1]) == list:
            for val in c[i][1]:
                t[val[1]] += val[0]*co
        else:
            t[c[i][1]] += co
    return [(t[x], x) for x in t]


x, y = 10, 53
xy = set([x, y])
solve(x, y)

for i in sorted(v.keys())[::-1]:
    flat = False
    for j in range(len(v[i])):
        if v[i][j][1] not in xy:
            v[i][j] = (v[i][j][0], v[v[i][j][1]])
            flat = True
    if flat:
        v[i] = flatten(v[i])

print(v)
