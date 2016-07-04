n, d, h = map(int, input().split())

if d > h * 2 or (n > 2 and h == 1 and d == 1):
    print(-1)
else:
    for i in range(2, h + 2):
        print(i-1, i)
    for i in range(d - h):
        if i == 0:
            print(1, h + 2)
        else:
            print(h + 2 + i - 1,  h + 2 + i)
    for i in range(d + 2, n + 1):
        print(h, i)
