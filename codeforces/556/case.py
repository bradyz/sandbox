n = int(input())
c = list(map(int, input()))
u = [False for v in c]
a, b = 0, 1
r = 0

while a >= 0 and a < n and b >= 0 and b < n:
    if c[a] + c[b] == 1:
        u[a] = True
        u[b] = True
        r += 2
    else:
        a += 1
        b += 1
    while a > 0 and a < n and u[a]:
        a -= 1
    while b < n and u[b]:
        b += 1
    if not u[a] and a == 0:
        while a < n and u[a]:
            a += 1

print(n - r)
