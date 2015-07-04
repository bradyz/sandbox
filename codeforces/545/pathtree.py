from sys import maxsize as INT_MAX

n, m = map(int, input().split())
c = {i: [] for i in range(1, m+1)}
d = [INT_MAX for _ in range(n+1)]
r = set()

for _ in range(m):
    x, y, z = map(int, input().split())
    c[x].append((y, z))
    c[y].append((x, z))

for i in c:
    c[i] = list(sorted(c[i], key=lambda x: x[1]))

print(c)

b = int(input())
d[b] = 0

for _ in range(n):
    u = []

print(c)
