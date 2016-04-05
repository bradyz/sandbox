from math import atan2, sqrt

for _ in range(int(input())):
    n = int(input())
    r = [list(map(int, input().split())) for _ in range(n)]
    a = {atan2(y, x): (x, y) for y, x in r}
    s = list(sorted(a.keys()))
    ret = 0
    for i in range(n):
        d = (a[s[i]][0] - a[s[(i-1) % n]][0]) ** 2 + \
            (a[s[i]][1] - a[s[(i-1) % n]][1]) ** 2
        ret = max(ret, d)
    print("%.3f" % sqrt(ret))
