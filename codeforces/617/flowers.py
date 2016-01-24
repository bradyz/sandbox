def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
n, x1, y1, x2, y2 = map(int, input().split())
coor = [list(map(int, input().split())) for _ in range(n)]
dist1 = [0] + list(map(lambda x: dist((x1, y1), x), coor))
dist2 = [0] + list(map(lambda x: dist((x2, y2), x), coor))
covered = [False for _ in dist1]
ret = 1e20
for i in range(n+1):
    max_dist2 = 0
    for j in range(n+1):
        if dist1[j] > dist1[i]:
            max_dist2 = max(max_dist2, dist2[j])
    ret = min(ret, dist1[i] + max_dist2)
print(ret)
