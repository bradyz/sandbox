from itertools import combinations


n, m = map(int, input().split())
g = [input().split() for _ in range(m)]
c = {i: set([i]) for i in range(n)}
for i in range(n):
    for j in range(i+1, n):
        can = True
        x, y = g[0][i], g[0][j]
        for k in range(1, m):
            x_i, y_i = g[k].index(x), g[k].index(y)
            if (i < j) ^ (x_i < y_i):
                can = False
                break
        if can:
            c[i].add(j)
            c[j].add(i)
r = 0
for u in c:
    for k in range(len(c[u])-1, r, -1):
        skip = False
        for s in combinations(c[u], k+1):
            can = True
            for i in range(len(s)):
                for j in range(i+1,len(s)):
                    if s[i] not in c[s[j]]:
                        can = False
                        break
                if not can:
                    break
            if can:
                r = max(r, len(s))
                skip = True
                break
        if skip:
            break
print(r)
