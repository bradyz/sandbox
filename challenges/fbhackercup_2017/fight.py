def parse(x):
    x, y = x.split("d")
    z = "0"
    if "+" in y:
        y, z = y.split("+")
    elif "-" in y:
        y, z = y.split("-")
        z = "-" + z
    return x, y, z


def solve(x, y, h):
    c = {a: 1 for a in range(1, y+1)}
    for i in range(1, x):
        d = dict()
        for j in range(1, y+1):
            for k, v in c.items():
                d[k+j] = d.get(k+j, 0) + v
        c = d
    return (sum(v for k, v in c.items() if k >= h) / sum(c.values()))


for t in range(1, int(input())+1):
    h, s = map(int, input().split())
    rolls = input().split()
    result = 0.0
    for i in range(s):
        x, y, z = map(int, parse(rolls[i]))
        result = max(result, solve(x, y, h - z))
    print("Case #%d: %.6f" % (t, result))
