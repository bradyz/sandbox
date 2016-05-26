from math import sqrt


ax, ay, bx, by, tx, ty = map(int, input().split())
n = int(input())
dist = list()
adist = list()
bdist = list()
for i in range(n):
    x, y = map(int, input().split())
    dist.append((tx - x) ** 2 + (ty - y) ** 2)
    # print(dist[i], (ax - x) ** 2 + (ay - y) ** 2)
    adist.append((dist[i] - ((ax - x) ** 2 + (ay - y) ** 2), i))
    bdist.append((dist[i] - ((bx - x) ** 2 + (by - y) ** 2), i))
adist.sort(reverse=True)
bdist.sort(reverse=True)
ret = 0
if adist[0][0] > 0 and bdist[0][0] > 0:
    used = set()
    if adist[0][1] == bdist[0][1]:
        if n > 1:
            if adist[0][0] + bdist[1][0] > adist[1][0] + bdist[0][0]:
                used.add(adist[0][1])
                used.add(bdist[1][1])
                ret += sqrt(dist[adist[0][1]] - adist[0][0])
                ret += sqrt(dist[bdist[1][1]] - bdist[1][0])
            else:
                used.add(adist[1][1])
                used.add(bdist[0][1])
                ret += sqrt(dist[adist[1][1]] - adist[1][0])
                ret += sqrt(dist[bdist[0][1]] - bdist[0][0])
        else:
            if adist[0][0] > bdist[0][0]:
                used.add(adist[0][1])
                ret += sqrt(dist[adist[0][1]] - adist[0][0])
            else:
                used.add(bdist[0][1])
                ret += sqrt(dist[bdist[0][1]] - bdist[0][0])
    else:
        used.add(adist[0][1])
        used.add(bdist[0][1])
        ret += sqrt(dist[adist[0][1]] - adist[0][0])
        ret += sqrt(dist[bdist[0][1]] - bdist[0][0])
    # print(used, ret)
    for i in range(n):
        if i in used:
            ret += sqrt(dist[i])
            continue
        ret += 2 * sqrt(dist[i])
else:
    used = set()
    if adist[0][0] < bdist[0][0]:
        used.add(adist[0][1])
        ret += sqrt(dist[adist[0][1]] - adist[0][0])
    else:
        used.add(bdist[0][1])
        ret += sqrt(dist[bdist[0][1]] - bdist[0][0])
    for i in range(n):
        if i in used:
            ret += sqrt(dist[i])
            continue
        ret += 2 * sqrt(dist[i])
print(dist)
print(adist[:2])
print(bdist[:2])
print(ret)
