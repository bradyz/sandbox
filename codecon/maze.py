n, m = map(int, input().split())
g = [list(input()) for _ in range(n)]
v = [[False for j in range(m)] for i in range(n)]


def dfs(x, y, p):
    if x < 0 or x >= n or y < 0 or y >= m:
        print("\n".join(map(lambda x: str(x[0])+","+str(x[1]), p[:-1])))
        return
    if g[x][y] == "X" or y >= m or v[x][y]:
        return
    v[x][y] = True
    if x != 1 and y != 0:
        dfs(x, y-1, p+[(x, y-1)])
    dfs(x+1, y, p+[(x+1, y)])
    dfs(x-1, y, p+[(x-1, y)])
    dfs(x, y+1, p+[(x, y+1)])

dfs(1, 0, [(1, 0)])
