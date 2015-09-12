def can_touch(x, y, a, b):
    for i, j in ((-1, -1), (1, 1), (1, -1), (-1, 1)):
        if x+i < 0 or x+i >= n or y+j < 0 or y+j >= m or g[x+i][y+j] == "*":
            continue
        elif x+i == a and y+j == b:
            return True
    return False


def combs(v, z):
    if v[0] == n-1:
        yield z
    else:
        t = False
        for x in z:
            if can_touch(v[0], v[1], x[0], x[1]):
                t = True
        if not t:
            for x in p[v[0]+1]:
                for y in combs(x, [v] + z):
                    yield y


if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    p = [[] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if g[i][j] == ".":
                p[i].append((i, j))

    r = 0

    for a in p[0]:
        for v in combs(a, []):
            print(r)
            r += 1

    print(r)
