n, m, start, x, y, end = map(int, input().split())
v = end - start
r = []

for i in range(m):
    if (v - (m - i) * y) % x == 0:
        r.append((v - (m-i) * y) // x + n)
        break

for i in range(n):
    if (v - (n - i) * x) % y == 0:
        r.append((v - (n-i) * x) // y + m)
        break

if not r:
    print("Impossible")
else:
    print(" ".join(map(str, r)))
