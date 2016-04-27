n, m, k = map(int, input().split())
c = list(map(int, input().split()))
r = 0
for _ in range(n):
    for x in map(int, input().split()):
        i = c.index(x)
        r += i + 1
        c.pop(i)
        c.insert(0, x)
print(r)
