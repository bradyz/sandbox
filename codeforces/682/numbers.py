n, m = map(int, input().split())
r = 0
for i in range(1, n+1):
    x = (5 - i) % 5
    if x == 0:
        r += (m - x) // 5
    else:
        r += (m - x) // 5 + 1
print(r)
