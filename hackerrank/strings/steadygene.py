n = int(input())
s = input()
pre = [{x: s[:i].count(x) for x in "ACTG"} for i in range(n+1)]
miss = {x: max(pre[n][x] - n // 4, 0) for x in "ACTG"}
best = n
for i in range(n):
    lo = i
    hi = n
    if sum((pre[hi][x]-pre[i][x]) < miss[x] for x in "ACTG") != 0:
        continue
    while lo < hi:
        mi = (lo + hi) // 2
        can = sum((pre[mi][x]-pre[i][x]) < miss[x] for x in "ACTG") == 0
        if can:
            hi = mi
        else:
            lo = mi + 1
    mi = (lo + hi) // 2
    if sum((pre[mi][x]-pre[i][x]) < miss[x] for x in "ACTG") == 0:
        best = min(best, mi - i)
print(best)
