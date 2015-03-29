for _ in range(int(input())):
    a = list(map(int, input().split()))
    x = 2*a[3] - a[1]
    y = 2*a[2] - a[0]
    print(str(y) + " " + str(x))
