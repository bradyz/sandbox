from math import sqrt
from math import ceil

for i in range(int(input())):
    n = int(input())
    r = [float(v) for v in input().split()]
    res = r[0]
    for j in range(1, n):
        if j == 0:
            res += r[j]
        else:
            tmp = sqrt((r[j] + r[j-1])**2 - (r[j] - r[j-1])**2)
            if tmp < r[j] or tmp < r[j-1]:
                res += max(r[j], r[j-1])
            else:
                res += sqrt((r[j] + r[j-1])**2 - (r[j] - r[j-1])**2)
            if j == n - 1:
                res += r[j]
    print(ceil(res))
