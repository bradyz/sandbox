prime = [True for _ in range(int(1e7))]
prime[0] = False
prime[1] = False
for i in range(2, len(prime)):
    if not prime[i]:
        continue
    for j in range(i + i, len(prime), i):
        prime[j] = False
r = (-1, -1)
m = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while prime[n * n + a * n + b]:
            n += 1
        if m < n - 1:
            m = n - 1
            r = (a, b)
print(m)
print(r)
