for _ in range(int(input())):
    n, x = map(int, input().split())
    m = list(map(int, input().split()))
    ret = 0
    for i in range(n):
        ret += max(0, m[i] - x)
    print(ret)
