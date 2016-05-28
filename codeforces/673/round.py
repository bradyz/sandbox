n, m = map(int, input().split())
a = set()
b = set()
for _ in range(m):
    x, y = map(int, input().split())
    if x < y:
        a.add(x)
        b.add(y)
    else:
        a.add(y)
        b.add(x)
if m == 0:
    print(n-1)
else:
    print(max(0, min(b) - max(a)))
