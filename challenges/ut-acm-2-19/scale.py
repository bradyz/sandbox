for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = 0
    ret = 0
    for i in range(n):
        if x <= a[i]:
            ret += 1
            x += a[i]
    print(ret)
