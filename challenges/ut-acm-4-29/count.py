for _ in range(int(input())):
    s = input()
    c = dict()
    o = 0
    for i in range(len(s)):
        if s[i] == "1":
            o += 1
        else:
            c[i] = o
    print(sum(c.values()))
