import sys


def has_cycle():
    def dfs(u):
        if u in vis:
            return False
        vis.add(u)
        seen.add(u)
        for v in g[u]:
            if v not in vis and dfs(v):
                return True
            elif v in seen:
                return True
        seen.remove(u)
        return False

    vis = set()
    seen = set()
    return any(dfs(x) for x in range(1, n+1))


sys.setrecursionlimit(10000)
n, m = map(int, input().split())
g = {u: list() for u in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
if not has_cycle():
    incoming = {u: 0 for u in range(1, n+1)}
    for u in g:
        for v in g[u]:
            incoming[v] += 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    top = [u for u in incoming if incoming[u] == 0]
    while top:
        u = top.pop()
        for v in g[u]:
            incoming[v] -= 1
            dp[v] = (dp[v] + dp[u]) % int(1e9)
            if incoming[v] == 0:
                top.append(v)
    print(dp[n])
else:
    print("INFINITE PATHS")
