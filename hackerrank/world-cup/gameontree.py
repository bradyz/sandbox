def solve():
    def dfs(x):
        if v[x]:
            return 0

        v[x] = True
        dp[x] += sum(dfs(y) for y in g[x])

        return dp[x]

    m = 0

    for i in range(1, n+1):
        dp = type(c)(c)
        v = [False for _ in range(n+1)]
        m = max(m, dfs(i) - max(dp[j] for j in g[i]))

    print(m)

if __name__ == "__main__":
    n = int(input())
    c = [0] + [int(v) for v in input().split()]
    g = {u: [] for u in range(1, n+1)}

    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    solve()
