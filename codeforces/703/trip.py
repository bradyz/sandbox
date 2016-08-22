n, k = map(int, input().split())
c = list(map(int, input().split()))
v = set(map(int, input().split()))
s = sum(c)
r = 0
for x in v:
    s -= c[x-1]
    r += s * c[x-1]
    c[x-1] = 0
for i in range(n):
    r += c[i] * c[(i+1) % n]
print(r)
