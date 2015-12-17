DIR = {"L": (0, -1), "R": (0, 1), "U": (-1, 0), "D": (1, 0)}
X, Y, x, y = map(int, input().split())
S = input()
path = list()
path.append((x, y))
for dx, dy in map(lambda x: DIR[x], S):
    xp, yp = x + dx, y + dy
    if xp < 1 or xp > X or yp < 1 or yp > Y:
        pass
    else:
        x, y = xp, yp
    path.append((x, y))
result = []
total = 0
vis = set()
for i in range(len(S)):
    if path[i] in vis:
        result.append(0)
    else:
        result.append(1)
        total += 1
    vis.add(path[i])
result.append(X * Y - total)
print(" ".join(map(str, result)))
