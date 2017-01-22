import sys
sys.setrecursionlimit(1000 * 1000)


DIR = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def dfs(x, y, v, c):
    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in v or g[x][y] != c:
        raise StopIteration
    v.add((x, y))
    yield (x, y)
    for dx, dy in DIR:
        yield from dfs(x + dx, y + dy, v, c)


m, n = map(int, input().split())

g = [input() for _ in range(m)]
z = [[-1 for _ in range(n)] for _ in range(m)]
counter = 0

v = set()
for i in range(m):
    for j in range(n):
        for x, y in dfs(i, j, v, "0"):
            z[x][y] = counter
        counter += 1

decimal = counter

v = set()
for i in range(m):
    for j in range(n):
        for x, y in dfs(i, j, v, "1"):
            z[x][y] = counter
        counter += 1

for _ in range(int(input())):
    x1, y1, x2, y2 = map(lambda x: int(x) - 1, input().split())

    if (z[x1][y1] == z[x2][y2]) and (z[x1][y1] >= decimal):
        print("decimal")
    elif (z[x1][y1] == z[x2][y2]) and (z[x1][y1] < decimal):
        print("binary")
    else:
        print("neither")
