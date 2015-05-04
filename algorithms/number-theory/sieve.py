n = 1000
a = [1 for _ in range(n)]
a[0], a[1], a[2] = 1, 1, 1
for i in range(2, n):
    if a[i] == 1:
        j = 2
        while i*j < n:
            a[i*j] = 0
            j += 1

b = [i for i, val in enumerate(a) if val == 1]
print(b)
