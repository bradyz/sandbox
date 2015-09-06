from queue import Queue


def solve():
    v = set()
    d = {}
    q = Queue()

    a = None

    for i in range(n):
        for j in range(m):
            if not a and g[i][j] == ".":
                a = (i, j)

    q.put((a, 0))

    while not q.empty():
        a, b = q.get()
        x, y = a

        d[b] = d.get(b, []) + [a]

        for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            if x+i < 0 or x+i >= n or y+j < 0 or y+j >= m or (x+i, y+j) in v or \
                    g[x+i][y+j] == "#":
                continue

            v.add((x+i, y+j))
            q.put(((x+i, y+j), b+1))

    r = 0

    for v in reversed(sorted(d.keys())):
        for w in d[v]:
            if r < k:
                g[w[0]][w[1]] = "X"
                r += 1

    print("\n".join(map(lambda x: "".join(x), g)))

n, m, k = map(int, input().split())
g = list(list(input()) for _ in range(n))

solve()
