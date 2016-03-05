from math import sqrt


for _ in range(int(input())):
    n = int(input())
    points = list()
    prev = 0
    for i, x in enumerate(map(int, input().split())):
        if i % 2 == 0:
            prev = x
        else:
            points.append((prev, x))
    points.sort()
    ret = 1e9
    for i in range(n):
        x1, y1 = points[i]
        for j in range(max(0, i-8), i):
            x2, y2 = points[j]
            dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
            if dist < ret:
                ret = dist
    print("{0:.4f}".format(sqrt(ret)))
