from sys import maxsize as INF


def solve(m):
    c = {}

    for v in m:
        if v in c:
            c[v] += 1
        else:
            c[v] = 1

    if not c:
        return 0

    d = sorted(c.keys())
    print(d, c)
    r = INF
    s = 1
    p = d[0]

    for v in d[1:]:
        if v == p+1 and c[v] == c[p]:
            s += 1
        else:
            r = min(r, s)
            s = 1
        p = v

    r = min(r, s)

    return r


t = int(input())

for _ in range(t):
    print(solve(list(map(int, input().split()))[1:]))
