from collections import defaultdict


def yes(a, b, x, y):
    if abs(a-x) <= 1 and abs(b - y) <= 1:
        return False
    return True


def solve(n, lamps, queries):
    r = list()
    du = defaultdict(set)
    dd = defaultdict(set)
    dx = defaultdict(set)
    dy = defaultdict(set)
    for x, y in lamps:
        du[y - x + 1].add((x, y))
        dd[y + x - 1].add((x, y))
        dx[x].add((x, y))
        dy[y].add((x, y))
    for x, y in queries:
        found = False
        for a, b in du.get(y - x + 1, set()):
            found |= yes(a, b, x, y)
        for a, b in dd.get(y + x - 1, set()):
            found |= yes(a, b, x, y)
        for a, b in dx.get(x, set()):
            found |= yes(a, b, x, y)
        for a, b in dy.get(y, set()):
            found |= yes(a, b, x, y)
        if found:
            r.append("LIGHT")
        else:
            r.append("DARK")
    return r


n = 8
lamps = [
        (1, 6),
        (5, 6),
        (7, 3),
        (3, 2)
]
queries = [
        (4, 4),
        (6, 6),
        (8, 1),
        (3, 2),
        (2, 3),
]
print(solve(n, lamps, queries))
