def powerset(d, c=[]):
    yield c
    for i in range(len(d)):
        for x in powerset(d[i+1:], c+[d[i]]):
            yield x


def solve():
    s = set((i, j) for i in range(n) for j in range(n) if g[i][j] == "B")
    m = n
    r = list(powerset(range(n)))
    c = r

    for r_i in r:
        for c_i in c:
            x = set((j, i) for i in range(n) for j in r_i)
            y = set((i, j) for i in range(n) for j in c_i)
            if not (s - x - y):
                m = min(m, len(r_i) + len(c_i))

    print(m)


if __name__ == "__main__":
    n = 8
    g = [list(input()) for _ in range(n)]

    solve()
