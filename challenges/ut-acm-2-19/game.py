for _ in range(int(input())):
    n, m, k = map(int, input().split())
    c = k
    for _ in range(m):
        l = input().split()
        if l[0] == "REVERSE":
            c = n - 1 - c
        else:
            u, v = int(l[1]), int(l[2])
            if u == c:
                c = v
            elif v == c:
                c = u
    print(c)
