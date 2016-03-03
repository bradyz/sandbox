n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = 0
for i in range(n):
    fa = a[i]
    fb = b[i]
    for j in range(i, n):
        fa |= a[j]
        fb |= b[j]
    r = max(r, fa+fb)
print(r)
