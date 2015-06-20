n, m = map(int, input().split())
c = sorted(list(map(int, input().split())))
d = sorted(list(map(int, input().split())))
r = 0
x, y = 0, 0
while x < n and y < n:
    if abs(c[x] - d[y]) <= m:
        r += 1
        x += 1
        y += 1
    else:
        if c[x] < d[y]:
            x += 1
        else:
            y += 1
print(r)
