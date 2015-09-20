def dfs(c):
    global r
    for x in g[c]:
        if v[x] == -1:
            v[x] = c
            dfs(x)


def calc(c, d):
    t = w[c][d]
    while c != d:
        t *= w[v[c]][c]
        c = v[c]
    return t

if __name__ == "__main__":
    n = int(input())
    g = {i: [] for i in range(1, n+1)}
    w = {i: {} for i in range(1, n+1)}
    v = [-1 for _ in range(n+1)]
    r = 0

    for i in range(1, n+1):
        x, y = map(int, input().split())
        g[i].append(x)
        w[i][x] = y / 100

    for i in range(1, n+1):
        if v[i] == -1:
            dfs(i)

    print("%.2f" % r)
