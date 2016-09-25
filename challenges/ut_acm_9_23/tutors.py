from math import floor


for _ in range(int(input())):
    n, m = map(int, input().split())
    val = [0 for _ in range(1001)]
    for _ in range(n):
        i, j = map(int, input().split())
        for x in range(i, j):
            val[x] += 1
    for _ in range(m):
        print(val[float(input()]))
