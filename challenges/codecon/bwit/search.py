from copy import deepcopy

n = int(input())
m = int(input())
g = [list(input().split()) for _ in range(n)]
c = list(input() for _ in range(m))
vis = [[False for j in range(n)] for i in range(n)]
res = set()


def sofar(small, big):
    if len(small) > len(big):
        return False
    i = 0
    while i < len(small):
        if small[i] != big[i]:
            return False
        i += 1
    return True


def dfs(x, y, path, v):
    if path == cur:
        return True
    if x < 0 or x >= n or y < 0 or y >= n or v[x][y]:
        return False
    if not sofar(path, cur):
        return False
    vis_copy = deepcopy(v)
    vis_copy[x][y] = True
    if dfs(x+1, y, path+g[x][y], vis_copy):
        return True
    if dfs(x-1, y, path+g[x][y], vis_copy):
        return True
    if dfs(x, y+1, path+g[x][y], vis_copy):
        return True
    if dfs(x, y-1, path+g[x][y], vis_copy):
        return True
    return False

for i in range(n):
    for j in range(n):
        for word in c:
            if word in res:
                continue
            cur = word
            vis_c = deepcopy(vis)
            if dfs(i, j, "", vis_c):
                vis = vis_c
                res.add(word)

for v in c:
    if v in res:
        print(v)
