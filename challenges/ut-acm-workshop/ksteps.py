def solve(b, e, k):
    def dfs(c, p):
        if c in v or e in v or p > k:
            return False
        elif c == e and p <= k and (k-p) % 2 == 0:
            return True

        v.add(c)
        r = any(dfs(x, p+1) for x in g[c])
        v.remove(c)

        return r

    v = set()

    return dfs(1, 0)


n, m = map(int, input().split())
g = {}

for _ in range(m):
    u, v = map(int, input().split())
    g[u] = g.get(u, set()) | set([v])
    g[v] = g.get(v, set()) | set([u])

for _ in range(int(input())):
    e, k = map(int, input().split())

    if solve(1, e, k):
        print(1)
    else:
        print(0)
