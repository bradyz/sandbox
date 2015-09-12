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
            for j in range(i+1, len(z)):
                if z[i] not in c[z[j]]:
                    return
        r += 1
        return

    for x in p[v[0]+1]:
        if x in c[v]:
            dfs(x, z + [x])

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    p = [[] for _ in range(n)]
    c = dict()

    for i in range(n):
        for j in range(m):
            if g[i][j] == ".":
                p[i].append((i, j))

    for i in range(n):
        for j in range(i+1, n):
            for x in p[i]:
                for y in p[j]:
                    if not can_touch(x[0], x[1], y[0], y[1]):
                        c[x] = c.get(x, set()) | set([y])
                        c[y] = c.get(y, set()) | set([x])

    r = 0

    for v in p[0]:
        dfs(v, [v])

    print(r)
