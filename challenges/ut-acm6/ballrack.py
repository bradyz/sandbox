from math import sqrt
from math import ceil

for i in range(int(input())):
    n = int(input())
    r = [int(v) for v in input().split()]
    x = [a for a in r] + [r[-1]]

    print(x)
    for j in range(n):
        if j == 0:
            if n > 1 and sqrt((r[j] + r[j+1])**2 - (r[j] - r[j+1])**2) < r[j+1]:
                x[j] = 0
        else:
            tmp = sqrt((r[j] + r[j-1])**2 - (r[j] - r[j-1])**2)
            x[j] = max(tmp, r[j], r[j-1])
            if j == n-1 and tmp > r[j] and r[j-1] > r[j]:
                x[j+1] = 0
        print(x)

    print(ceil(sum(x)))
    print()
