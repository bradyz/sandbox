def solve():
    def dfs(x, y):
        for a, b in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if x+a < 0 or x+a >= n or y+b < 0 or y+b >= m or (x+a, y+b) in p or \
                    g[x+a][y+b] == "#":
                continue

            p[(x+a, y+b)] = (x, y)
            dfs(x+a, y+b)

    p = dict()

    for i in range(n):
        for j in range(m):
            if g[i][j] == ".":
                dfs(i, j)
                break

    for i in range(k):
        s = list(set(p.keys()) - set(p.values()))
        if s:
            x, y = s[0]
            g[x][y] = "X"
            p.pop(s[0])

    print("\n".join(map(lambda x: "".join(x), g)))

n, m, k = map(int, input().split())
g = list(list(input()) for _ in range(n))
solve()
