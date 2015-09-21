n, m = map(int, input().split())
if n > m:
    m, n = n, m
k = 1
while (k*m) % n != 0:
    k += 1
print(k*m)
