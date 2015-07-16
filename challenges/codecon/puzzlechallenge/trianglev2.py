import sys

g = [line.strip() for line in sys.stdin]
n = len(g)
r = 0

def solve():
    global g, n, r
    for i in range(n):
        for j in range(n):
            t = g[i][j]
            for k in range(1, n-j+1):
                x = 0
                while x <= k and j+x < n and i-x >= 0 and i-k+x < n and j+x < n and g[i][j+x] == t and g[i-x][j] == t and g[i-k+x][j+x] == t:
                    x += 1
                if x > k:
                    r = max(r, x * (x+1) // 2)
                x = 0
                while x <= k and j+x < n and i-x >= 0 and j+k < n and i-x >= 0 and j+x < n and g[i][j+x] == t and g[i-x][j+k] == t and g[i-x][j+x] == t:
                    x += 1
                if x > k:
                    r = max(r, x * (x+1) // 2)

solve()
g = list(reversed(g))
solve()
print(r)
