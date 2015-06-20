n = 2000001
c = [True for i in range(n)]
for i in range(2, n):
    j = 2
    if c[i]:
        while i * j < n:
            c[i*j] = False
            j += 1
r = 0
for i in range(2, n-1):
    if c[i]:
        r += i
print(r)
