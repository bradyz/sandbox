def solve():
    def dfs(x, y):
        s.add(x)
        if y > m:
            return 0
        if not g[x] - s:
            return 1
        return sum(dfs(v, (c[v] == 1 and y)+c[v]) for v in g[x] if v not in s)

    s = set()
    print(dfs(1, c[1]))

if __name__ == "__main__":
    n, m = map(int, input().split())
    c = [0] + list(map(int, input().split()))
    g = {i: set() for i in range(1, n+1)}
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u].add(v)
        g[v].add(u)
    solve()
