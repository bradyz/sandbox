n = int(input())
k = int(input())
c = [int(input()) for _ in range(n)]
c.sort()
p = [0] + c[::]
for i in range(1, n+1):
    p[i] += p[i-1]
print(c)
print(p)
m = 1e9
for x in range(k-1, n):
    r = 0
    for i in range(x - k + 1, x + 1):
        for j in range(i + 1, x + 1):
            r += abs(c[i] - c[j])
    m = min(m, r)
    print(c[x] - c[x-k+1], r)
print(m)
