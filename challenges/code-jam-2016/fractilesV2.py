for t in range(1, int(input()) + 1):
    k, c, s = map(int, input().split())

    ret = []
    if c == 1:
        for i in range(k):
            ret.append(i+1)
    else:
        a = 0
        while len(ret) < s:
            ret.append(a + 1)
            a += k ** (c - 1)

    print("Case #%d:" % t, " ".join(map(str, ret)))
