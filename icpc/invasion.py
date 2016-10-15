for _ in range(int(input())):
    c = list(map(int, input().split()))
    i = len(c)-1
    while i > 0:
        c[i-1] += c[i] // 2
        c[i] = c[i] % 2
        i -= 1
    print(" ".join(map(str, c)))
