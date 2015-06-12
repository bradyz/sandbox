n = int(input())
r = 0


def dfs(x, y, l):
    global r, n
    if l > n or (x > 2 and y != 1) or x < 0 or y < 0 or x > 3 or y > 2:
        return
    if x == 2 and y == 2 and l == n:
        r += 1
    dfs(x-1, y+2, l+1)
    dfs(x-1, y-2, l+1)
    dfs(x+1, y+2, l+1)
    dfs(x+1, y-2, l+1)
    dfs(x-2, y+1, l+1)
    dfs(x-2, y-1, l+1)
    dfs(x+2, y+1, l+1)
    dfs(x+2, y-1, l+1)

dfs(0, 0, 0)
print(r)
