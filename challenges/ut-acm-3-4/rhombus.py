for _ in range(int(input())):
    r, c = map(int, input().split())
    g = [input() for _ in range(r)]
    ret = 0
    cont = True
    doit = list()
    for i in range(r):
        for j in range(c):
            if g[i][j] == "1":
                doit.append((i, j))
    for n in range(100):
        if not cont:
            break
        new = list()
        for i, j in doit:
            can = True
            for x in range(r):
                if not can:
                    break
                for y in range(c):
                    if abs(i-x) + abs(j-y) > (n) // 2:
                        continue
                    if g[x][y] == "0":
                        can = False
                        break
            if can:
                ret = n
                new.append((i, j))
        doit = new
    print(ret)
