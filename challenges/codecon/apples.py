n, m, start, x, y, end = map(int, input().split())
v = end - start
r = []
print(n*x+m*y+start)

for i in range(m * y // x, -1, -1):
    t = start - i * x
    if (end - t) % y == 0 and ((end - t) // y) <= m:
        r.append(n+i)
        break

for i in range(n * x // y, -1, -1):
    t = start - i * y
    if (end - t) % x == 0 and ((end - t) // x) <= n:
        r.append(m+i)
        break

if len(r) < 2:
    print("Impossible")
else:
    print(" ".join(map(str, r)))
