def solve():
    t = dict()
    v = set(d.keys())
    x = 0
    for key, val in g.items():
        t[key] = type(val)(val)
    while v:
        s = type(v)(v)
        t_x = -1
        for u in t:
            s -= t[u]
        for u in s:
            t_x = max(t_x, x+d[u][0])
            if x + d[u][0] > d[u][1]:
                return "NO"
            t.pop(u)
        x = t_x
        v -= s
    if x > w:
        return "NO"
    return "YES"

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m, w = map(int, input().split())
        d = dict()
        g = dict()

        for _ in range(n):
            s, b, c = input().split()
            d[s] = (int(b), int(c))
            g[s] = set()

        for _ in range(m):
            u, v = input().split()
            g[u].add(v)

        print(solve())
