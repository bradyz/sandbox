n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
x, y = -1, -1
for i in range(n):
    for j in range(m):
        if g[i][j] == "*":
            x, y = i, j

q = [(x, y, 0)]
v = set([x, y])
r = -1
while q:
    cx, cy, cz = q.pop(0)
    if g[cx][cy] == "S":
        r = cz
        break
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = cx + dx, cy + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif g[nx][ny] == "X":
            continue
        elif (nx, ny) in v:
            continue
        v.add((nx, ny))
        q.append((nx, ny, cz + 1))
print(r)
