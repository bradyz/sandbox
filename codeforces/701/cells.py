n, m = map(int, input().split())
col = [False for _ in range(n)]
row = [False for _ in range(n)]
c = 0
r = 0
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    if not row[x]:
        r += 1
    if not col[y]:
        c += 1
    row[x] = True
    col[y] = True
    print(n * n - (r * n + c * n - r * c))
