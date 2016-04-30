for _ in range(int(input())):
    r, c, o = map(int, input().split())
    g = [list(input()) for _ in range(r)]
    for _ in range(o):
        s, x = input().split()
        x = int(x)
        if s == "R":
            for i in range(0, r, x):
                for j in range(c):
                    if g[i][j] == "0":
                        g[i][j] = "1"
                    else:
                        g[i][j] = "0"
        else:
            for i in range(0, c, x):
                for j in range(r):
                    if g[j][i] == "0":
                        g[j][i] = "1"
                    else:
                        g[j][i] = "0"
    print("\n".join(map(lambda x: "".join(x), g)))
