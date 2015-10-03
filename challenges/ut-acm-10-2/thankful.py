for j in range(int(input())):
    c = [input() for _ in range(int(input()))]
    x = 0
    y = 0

    for v in c:
        t = list(v)
        if t[0] == "-":
            for i in range(1, len(v)):
                if v[i] == "#":
                    if i == 1:
                        t[i] = "1"
                    else:
                        t[i] = "0"
        else:
            for i in range(len(v)):
                if v[i] == "#":
                    t[i] = "9"
        x += int("".join(t))

    for v in c:
        t = list(v)
        if t[0] == "-":
            for i in range(1, len(v)):
                if v[i] == "#":
                    t[i] = "9"
        else:
            for i in range(len(v)):
                if v[i] == "#":
                    if i == 0:
                        t[i] = "1"
                    else:
                        t[i] = "0"
        y += int("".join(t))

    print("Case " + str(j+1) + ": " + str(y) + " " + str(x))
