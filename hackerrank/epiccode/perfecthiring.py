n, p, x = map(int, input().split())
c = list(map(int, input().split()))
d = [0 for _ in range(n)]

for i in range(n):
    d[i] = p * c[i]
    p -= x

m = 0
for i in range(n):
    if d[i] > d[m]:
        m = i
print(m+1)
