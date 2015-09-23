n = 8
g = [list(input()) for _ in range(n)]
r = set()
c = set()

for i in range(n):
    if g[i].count("B") == n:
        r.add(i)
    else:
        c |= set(j for j in range(n) if g[i][j] == "B")

print(len(r) + len(c))
