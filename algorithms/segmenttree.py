INF = 1e9


class SegmentTree(object):
    def __init__(self, values):
        self.n = len(values)
        self.values = values

        self.tree = [0 for _ in range(2 * self.n - 1)]

        self._build(0, 0, self.n-1)

    def _build(self, i, a, b):
        if b < a:
            return INF

        if a == b:
            self.tree[i] = self.values[a]
        else:
            l = self._build(2 * i + 1, a, (a + b) // 2)
            r = self._build(2 * i + 2, (a + b) // 2 + 1, b)

            self.tree[i] = min(l, r)

        return self.tree[i]

    def query(self, l, r):
        return self._query(0, 0, self.n-1, l, r)

    def update(self, l, r, v):
        return self._update(0, 0, self.n-1, l, r, v)

    # query over [l, r]
    def _query(self, i, a, b, l, r):
        if b < a:
            return INF
        elif b < l or r < a:
            return INF
        elif a >= l and b <= r:
            return self.tree[i]

        lhs = self._query(2 * i + 1, a, (a + b) // 2, l, r)
        rhs = self._query(2 * i + 2, (a + b) // 2 + 1, b, l, r)

        return min(lhs, rhs)

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

        self.tree[i] = min(self.tree[2 * i + 1], self.tree[2 * i + 2])


def test(val, tree):
    result = [tree.query(i, i) for i in range(len(val))]

    print(val)
    print(result)

    for i in range(len(val)):
        for j in range(i, len(val)):
            assert min(val[i:j+1]) == tree.query(i, j)


if __name__ == "__main__":
    val = [100 for _ in range(8)]
    tree = SegmentTree(val)

    # Vanilla test.
    test(val, tree)

    l = 2
    r = 5
    v = -10

    for i in range(l, r+1):
        val[i] += v

    tree.update(l, r, v)

    # Update test.
    test(val, tree)
