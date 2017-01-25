n, m, k, x, y = map(int, input().split())
c = [[0 for _ in range(m)] for _ in range(n)]

if n == 1 or n == 2:
    full = m * n
else:
    full = (m * (2 * n - 2))

calls = k // full
k -= calls * full

for i in range(n):
    for j in range(m):
        if i == 0 or i == n-1:
            c[i][j] = calls
        else:
            c[i][j] = 2 * calls

cx, cy = 0, 0
dx = 1

for i in range(k):
    c[cx][cy] += 1
    if cy + 1 == m:
        if cx == n-1:
            dx = -1
        cx += dx
    cy = (cy + 1) % m

print(max(max(c)), min(min(c)), c[x-1][y-1])
