D = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, v):
    if x < 0 or x >= r or y < 0 or y >= c:
        return 0
    elif g[x][y] == 0:
        return 0
    elif (x, y) in v:
        return 0
    v.add((x, y))
    ret = g[x][y]
    for dx, dy in D:
        ret += dfs(x+dx, y+dy, v)
    return ret

for _ in range(int(input())):
    sr, sc, r, c = map(int, input().split())
    ret = list()
    for _ in range(3):
        g = [list(map(int, input().split())) for _ in range(r)]
        ret.append(dfs(sr, sc, set()))
    print(" ".join(map(str, ret)))
