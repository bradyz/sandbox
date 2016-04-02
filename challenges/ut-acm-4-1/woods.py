for _ in range(int(input())):
    n = int(input())
    c = list(sorted(map(int, input().split())))
    ret = 1
    for i in range(n):
        ret = (ret * (c[i] - i)) % 1000000007
    print(ret)
