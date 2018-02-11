class SegmentTree(object):
    def __init__(self, values):
        self.n = len(values)
        self.values = values

        self.tree = [0 for _ in range(2 * self.n - 1)]

        self._build(0, 0, self.n-1)

    def _build(self, i, a, b):
        if b < a:
            return 0

        if a == b:
            self.tree[i] = self.values[a]
        else:
            l = self._build(2 * i + 1, a, (a + b) // 2)
            r = self._build(2 * i + 2, (a + b) // 2 + 1, b)

            self.tree[i] = l + r

        return self.tree[i]

    def query(self, l, r):
        return self._query(0, 0, self.n-1, l, r)

    def update(self, l, r, v):
        return self._update(0, 0, self.n-1, l, r, v)

    # query over [l, r]
    def _query(self, i, a, b, l, r):
        if b < a:
            return 0
        elif b < l or r < a:
            return 0
        elif a >= l and b <= r:
            return self.tree[i]

        lhs = self._query(2 * i + 1, a, (a + b) // 2, l, r)
        rhs = self._query(2 * i + 2, (a + b) // 2 + 1, b, l, r)

        return lhs + rhs

    def _update(self, i, a, b, l, r, v):
        if b < a:
            return
        elif b < l or r < a:
            return
        elif a == b:
            self.tree[i] += v
            return

        self._update(2 * i + 1, a, (a + b) // 2, l, r, v)
        self._update(2 * i + 2, (a + b) // 2 + 1, b, l, r, v)

        self.tree[i] = self.tree[2 * i + 1] + self.tree[2 * i + 2]


tree = SegmentTree([0 for _ in range(int(2 ** 20))])

segments, queries = map(int, input().split())

for _ in range(segments):
    u, v = map(int, input().split())

    tree.update(u, v-1, 1)

for _ in range(queries):
    t = int(input())

    print(tree.query(t, t))
