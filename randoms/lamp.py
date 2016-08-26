def solve(n, lamps, queries):
    r = list()
    for x, y in queries:
        found = False
        for a, b in lamps:
            if abs(x - a) <= 1 and abs(y - b) <= 1:
                continue
            if x == a or y == b:
                found = True
            elif abs(x - a) % abs(y - b) == 0 and \
                    abs(x - a) // abs(y - b) in [-1, 1]:
                found = True
            if found:
                break
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
