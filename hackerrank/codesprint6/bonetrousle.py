for _ in range(int(input())):
    n, k, b = map(int, input().split())
    if b * (k - b) + (b * (b + 1)) // 2 < n:
        print(-1)
    elif (b * (b + 1)) // 2 > n:
        print(-1)
    else:
        i = (n - (b * (b + 1) // 2)) // b + 1
        c = list(range(i, i + b))
        s = sum(c)
        j = 1
        while s != n and j <= len(c):
            tmp = min(c[-j] + n - s, k - j + 1) - c[-j]
            c[-j] = min(c[-j] + n - s, k - j + 1)
            s += tmp
            j += 1
        print(" ".join(map(str, c)))
