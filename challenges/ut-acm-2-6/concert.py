DIR = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def dfs(x, y):
    ret = g[x][y]
    v[x][y] = True
    stack = [(x, y)]
    while stack:
        x, y = stack.pop()
        for dx, dy in DIR:
            xp, yp = x + dx, y + dy
            if xp < 0 or xp >= r or yp < 0 or yp >= c or v[xp][yp] or g[xp][yp] == 0:
                continue
            ret += g[xp][yp]
            v[xp][yp] = True
            stack.append((xp, yp))
    return ret

for _ in range(int(input())):
    r, c = map(int, input().split())
    x, y = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(r)]
    v = [[False for _ in range(c)] for _ in range(r)]
    print(dfs(x, y))
