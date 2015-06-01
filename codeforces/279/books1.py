n, t = map(int, input().split())
c = list(map(int, input().split()))
for i in range(1, n):
    c[i] += c[i-1]
x, y = -1, 0
m = 0
while y < n:
    if x == -1:
        if c[y] <= t:
            m = max(m, y + 1)
            y += 1
        else:
            x += 1
    elif c[y] - c[x] <= t:
        m = max(m, y - x)
        y += 1
    else:
        x += 1
print(m)
