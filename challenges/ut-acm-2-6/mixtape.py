for _ in range(int(input())):
    n, b = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    r = 0
    for i, j in zip(x, y):
        r += i * j
    if r >= b:
        print("YES")
    else:
        print("NO")
