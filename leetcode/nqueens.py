def solve():
    def check(c, s):
        for d in s:
            if d[0] == c[0] or d[1] == c[1] or (d[1]-c[1]) / (d[0]-c[0]) == -1 \
                    or (d[1]-c[1]) / (d[0]-c[0]) == 1:
                return False
        return True

    def recur(r, c, s, g):
        if r != -1 and c != -1:
            g[r][c] = "Q"

        if r == n-1:
            p(g)

        for i in range(n):
            if check((r+1, i), s):
                recur(r+1, i, s | set([(r+1, i)]),
                      [[col for col in row] for row in g])

    p = lambda x: print("\n".join(map(str, x)))

    recur(-1, -1, set(), [["." for _ in range(n)] for _ in range(n)])

if __name__ == "__main__":
    n = 6
    solve()
