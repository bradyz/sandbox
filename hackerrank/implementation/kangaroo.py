x1, v1, x2, v2 = map(int, input().split())
r = False
for i in range(1, 10001):
    if (v2 * i + (x2 - x1)) % v1 == 0:
        r = True
if r:
    print("YES")
else:
    print("NO")
