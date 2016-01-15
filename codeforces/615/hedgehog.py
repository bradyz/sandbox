n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]
count = [0 for _ in range(n+1)]
dp = [0 for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    if v < u:
        u, v = v, u
    graph[v].append(u)
    count[v] += 1
    count[u] += 1
for i in range(1, n+1):
    best = 1
    for j in graph[i]:
        best = max(best, dp[j] + 1)
    dp[i] = best
result = 1
for i in range(1, n+1):
    if dp[i] * count[i] > result:
        result = dp[i] * count[i]
print(result)
