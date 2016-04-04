from math import atan2, sqrt

for _ in range(int(input())):
    n = int(input())
    r = [list(map(int, input().split())) for _ in range(n)]
    a = {atan2(y, x): (x, y) for y, x in r}
    s = list(sorted(a.keys()))
    ret = 1e9
    print(a)
    for i in range(n):
        print(i, (i-1) % n)
        d = (a[s[i]][0] - a[s[(i-1) % n]][0]) ** 2 + \
            (a[s[i]][1] - a[s[(i-1) % n]][1]) ** 2
        ret = min(ret, d)
    print("%.3f" % sqrt(ret))
