from math import sqrt


ax, ay, bx, by, tx, ty = map(int, input().split())
n = int(input())
dist = list()
adist = list()
bdist = list()
for i in range(n):
    x, y = map(int, input().split())
    dist.append((tx - x) ** 2 + (ty - y) ** 2)
    if dist[-1] + (ax - x) ** 2 + (ay - y) ** 2 < dist[-1] * 2:
        adist.append((dist[-1] + (ax - x) ** 2 + (ay - y) ** 2, i))
    if dist[-1] + (bx - x) ** 2 + (by - y) ** 2 < dist[-1] * 2:
        bdist.append((dist[-1] + (bx - x) ** 2 + (by - y) ** 2, i))
found = [False for _ in range(n)]
adist.sort()
bdist.sort()
besta = 0
bestb = 0
if len(adist) == 0:
    besta = -1
if len(bdist) == 0:
    bestb = -1
while besta >= 0 and bestb >= 0 and adist[besta][1] == bdist[bestb][1]:
    if adist[besta][0] < bdist[bestb][0]:
        bestb += 1
    else:
        besta += 1
print(adist, besta)
print(bdist, bestb)
print(dist)
ret = 0
ret += adist[besta][0]
print(ret)
ret += bdist[bestb][0]
print(ret)
for i in range(n):
    if i == adist[besta][1] or i == bdist[bestb][1]:
        continue
    print(i)
    ret += dist[i] * 2
print(sqrt(ret))
