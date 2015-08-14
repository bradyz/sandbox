n, m = map(int, input().split())
c = [0 for _ in range(n)]
for _ in range(m):
    t = list(map(int, input().split()))
    c[t.index(max(t))] += 1
print(c.index(max(c))+1)
