def can_touch(x, y, a, b):
    for i, j in ((-1, -1), (1, 1), (1, -1), (-1, 1)):
        if x+i < 0 or x+i >= n or y+j < 0 or y+j >= m or g[x+i][y+j] == "*":
            continue
        elif x+i == a and y+j == b:
            return True
    return False

def dfs(v, z):
    global r

    if v[0] == n-1:
        for i in range(len(z)):
            for j in range(i + 1, len(z)):
                if z[i] not in c[z[j]]:
                    return
        r += 1
        return
    elif v not in c:
        return

    for x in c[v]:
        if x[0] == v[0] + 1:
            dfs(x, z + [x])

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    p = []
    c = dict()

    for i in range(n):
        for j in range(m):
            if g[i][j] == ".":
                p.append((i, j))

    for i in range(len(p)):
        x1, y1 = p[i]
        for j in range(i+1, len(p)):
            x2, y2 = p[j]
            if not can_touch(x1, y1, x2, y2):
                c[(x1, y1)] = c.get((x1, y1), []) + [(x2, y2)]
                c[(x2, y2)] = c.get((x2, y2), []) + [(x1, y1)]

    r = 0

    for v in p:
        if v[0] == 0:
            dfs(v, [v])

    print(r)
