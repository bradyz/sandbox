x, y, t, n = map(int, input().split())
p = [tuple(input().split()) for _ in range(n)]
from_hospital = dict()
from_hospital[(x, y)] = 0
q = [(x, y)]
vis = set([(x, y)])
while q:
    cx, cy = q.pop(0)
    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nx, ny = cx + dx, cy + dy
        if nx < 0 or ny < 0 or nx > 100 or ny > 100:
            continue
        elif nx % 10 != 0 and ny % 10 != 0:
            continue
        elif (nx, ny) in vis:
            continue
        from_hospital[(nx, ny)] = from_hospital[(cx, cy)] + 1
        vis.add((nx, ny))
        q.append((nx, ny))
dists = list()
for v in p:
    coord = tuple(map(int, v[1:]))
    dists.append((v[0], from_hospital[coord]))
dists.sort(key=lambda x: x[1])
result = list()
for x in dists:
    if t - 2 * x[1] < 0:
        break
    t -= 2 * x[1]
    result.append(x[0])
result.sort()
print(str(len(result)) + " " + " ".join(result))
