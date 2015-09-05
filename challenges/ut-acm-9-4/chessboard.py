def solve():
    def neighbors(i, j):
        if g[i][j] == ".":
            return []

        r = []

        if i-1 >= 0 and g[i-1][j] != "." and g[i][j] ^ g[i-1][j]:
            r.append((i-1, j))
        if j-1 >= 0 and g[i][j-1] != "." and g[i][j] ^ g[i][j-1]:
            r.append((i, j-1))
        if i+1 < n and g[i+1][j] != "." and g[i][j] ^ g[i+1][j]:
            r.append((i+1, j))
        if j+1 < n and g[i][j+1] != "." and g[i][j] ^ g[i][j+1]:
            r.append((i, j+1))

        return r

    r = 0

    while True:
        c = [(i, j, neighbors(i, j)) for i in range(n) for j in range(n)]
        d = {(i, j): neighbors(i, j) for i in range(n) for j in range(n)}

        c.sort(key=lambda x: len(x[2]))

        x = -1

        for v in c:
            if len(v[2]) > 0:
                x = v
                break
        else:
            break

        a = None

        for v in x[2]:
            if not a or len(d[v]) > len(d[a]):
                a = v

        g[x[0]][x[1]] = "."
        g[a[0]][a[1]] = "."

        r += 2

    print(r)

n = 8

for _ in range(int(input())):
    g = [list(input()) for _ in range(n)]

    for i in range(n):
        for j in range(n):
            g[i][j] = g[i][j] == "U"

    solve()
