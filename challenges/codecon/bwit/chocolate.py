cost = int(input())
wrap = int(input())
n = int(input())



for _ in range(n):
    p = int(input())
    count = 0
    w = 0
    while p > 0:
        count += 1
        w += 1
        if wrap > 0 and w % wrap == 0:
            count += 1
            w += 1
        p -= cost
    print(count)
