def can(x, y, c, b):
    if (x, y) in c:
        return False
    elif (x, y) in b:
        return False
    elif x < 0 or x >= 5:
        return False
    elif y < 0 or y >= 5:
        return False
    return True


def move(x, y, c, b):
    moves = list()
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        rx, ry = x + dx, y + dy
        nx, ny = x + 2 * dx, y + 2 * dy
        if (rx, ry) in c and can(nx, ny, c, b):
            moves.append((nx, ny, rx, ry))
    return moves


def solve(p, b):
    r = len(p)
    v = set()
    s = [p]
    while s:
        c = s.pop()
        r = min(r, len(c))
        if c in v:
            continue
        v.add(frozenset(c))
        for x, y in c:
            for nx, ny, rx, ry in move(x, y, c, b):
                d = set(c)
                d.remove((x, y))
                d.remove((rx, ry))
                d.add((nx, ny))
                s.append(d)
    print("The best case ends with %d pegs." % r)


for _ in range(int(input())):
    g = [input() for _ in range(5)] 
    p = set([(i, j) for i in range(5) for j in range(5) if g[i][j] == "o"])
    b = set([(i, j) for i in range(5) for j in range(5) if g[i][j] == "#"])
    solve(p, b)
