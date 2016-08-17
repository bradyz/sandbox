n, m = map(int, input().split())
g = {u: list() for u in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
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
if incoming[n] != 0:
    print("INFINITE PATHS")
else:
    print(dp[n])
