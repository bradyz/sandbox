from sys import maxsize as MAXINT


def p():
    print("\n".join(map(str, g)))


def can(x, y):
    return x >= 0 and x < m and y >= 0 and y < n


def solve():
    def dfs(i, j, c, m):
        r = False
        if m == 0 or m == 1:
            if g[i][j] <= c:
                return False
            for x, y in d:
                if can(i+x, j+y) and g[i][j] + 1 >= g[i+x][j+y] and \
                        g[i+x][j+y] > c and not v[i+x][j+y]:
                    if g[i+x][j+y] == h:
                        return True
                    v[i+x][j+y] = True
                    r |= dfs(i+x, j+y, c, m+1)
                    v[i+x][j+y] = False
        else:
            if b.get((i, j), MAXINT) < c:
                return False
            b[(i, j)] = c
            if c == -1:
                r |= dfs(i, j, l, 0)
            else:
                r |= dfs(i, j, c+1, 0)
        return r

    b = dict()
    v = [[False for _ in range(n)] for _ in range(m)]
    if dfs(s_x, s_j, -1, 0):
        return True
    return False


d = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if i != 0 or j != 0]
for c_t in range(int(input())):
    m, n = map(int, input().split())
    g = [list(input()) for _ in range(m)]
    l = MAXINT
    s_x, s_y = -1, -1
    h = -1
    for i in range(m):
        for j in range(n):
            if g[i][j].isalpha():
                g[i][j] = 10 + ord(g[i][j]) - ord("A")
            else:
                g[i][j] = int(g[i][j])
            if g[i][j] < l:
                s_x = i
                s_j = j
                l = g[i][j]
            h = max(h, g[i][j])
    if solve():
        print("Case " + str(c_t+1) + ": SAFE")
    else:
        print("Case " + str(c_t+1) + ": MELTED")
