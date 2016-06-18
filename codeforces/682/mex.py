n = int(input())
c = list(map(int, input().split()))
c.sort()
m = 1
for i in range(n):
    if m <= c[i]:
        c[i] = m
        m += 1
print(m)
