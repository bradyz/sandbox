n, t = map(int, input().split())
c = list(map(int, input().split()))
u, s, z = 0, 0, 0
for v in range(n):
    s += c[v]
    while s > t:
        s -= c[u]
        u += 1
    z = max(z, v-u+1)
print(z)
