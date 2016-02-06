for _ in range(int(input())):
    n, x, y = map(int, input().split())
    c = [int(input()) for _ in range(n)]
    if x + (max(c) - min(c)) * y > n * x:
        print(n * x)
    else:
        print(x + n * y)
