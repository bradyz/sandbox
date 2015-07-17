import sys

g = [list(line.strip()) for line in sys.stdin]
n = len(g)
m = len(g[0])
r = 0


def solve():
    global g, n, m, r
    for i in range(n):
        for j in range(m):
            t = g[i][j]
            for k in range(1, m-j+1):
                x = 0
                while x <= k and i-x >= 0 and i-k+x >= 0 and i-k+x < n and j+x < m and g[i][j+x] == t and g[i-x][j] == t and g[i-k+x][j+x] == t:
                    x += 1
                if x > k:
                    r = max(r, x * (x + 1) // 2)

                x = 0
                while x <= k and i-x >= 0 and j+x < m and j+k < m and g[i][j+x] == t and g[i-x][j+k] == t and g[i-x][j+x] == t:
                    x += 1
                if x > k:
                    r = max(r, x * (x + 1) // 2)

                x = 0
                while x <= k and j+x < m and j+k+x < m and i-x >= 0 and i-k+x >= 0 and g[i][j+x] == t and g[i][j+k+x] == t and g[i-x][j+x] == t and g[i-k+x][j+x+k] == t:
                    x += 1
                if x > k:
                    r = max(r, (2 * k + 2) * (k + 1) // 2)

solve()

g = list(map(lambda x: list(reversed(x)), g))
solve()

g = list(zip(*g))
n, m = m, n
solve()

g = list(reversed(g))
solve()

print(r)
