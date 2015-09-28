n, k = map(int, input().split())
c = list(map(int, input().split()))

a = [1 for v in c]
b = [1 for v in c]

for i in range(1, n):
    if c[i] >= c[i-1]:
        a[i] = min(a[i-1] + 1, k)
    if c[i] <= c[i-1]:
        b[i] = min(b[i-1] + 1, k)

print(c)
print(a)
print(b)

x = 0
y = 0

for i in range(1, n):
    if a[i] != 1 and a[i] <= a[i-1] or i == k-1:
        x += (a[i]-1) * a[i] // 2
    if b[i] != 1 and b[i] >= b[i-1]:
        y += (b[i]-1) * b[i] // 2

    if i > k:
        if a[i-k-1] <= a[i-k]:
            print(a[i-k])
            x -= (a[i-k]-1) * a[i-k] // 2
        if b[i-k-1] <= b[i-k]:
            y -= (b[i-k]-1) * b[i-k] // 2

    print(i, x, y)
