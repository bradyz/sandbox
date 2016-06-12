n = int(input())
s = input()
pre = [{x: s[:i].count(x) for x in "ACTG"} for i in range(n+1)]
miss = {x: max(pre[n][x] - n // 4, 0) for x in "ACTG"}
# print(miss)
best = n
for i in range(n):
    lo = i
    hi = n
    if sum((pre[hi][x]-pre[i][x]) < miss[x] for x in "ACTG") != 0:
        continue
    print(s[i:hi])
    while lo < hi:
        mi = (lo + hi) // 2
        can = sum((pre[mi][x]-pre[i][x]) < miss[x] for x in "ACTG") == 0
        print(s[i:mi], can, lo, hi, mi)
        if can:
            best = min(best, mi - i)
            hi = mi
        else:
            lo = mi + 1
    print()
    # print(s[i:mi])
    if sum((pre[mi][x]-pre[i][x]) < miss[x] for x in "ACTG") == 0:
        # print(s[i:mi])
        best = min(best, mi - i)
    # print()
print(best)
    # for j in range(i+1, n+1):
    #     print(s[i:j], diff(pre[j], pre[i]))
