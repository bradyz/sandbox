from random import randrange


INF = 1e9
N = 100000
tree = [0 for _ in range(N)]


# build over [a, b]
def build(i, a, b):
    if b < a:
        return INF
    elif a == b:
        tree[i] = val[a]
    else:
        l = build(2 * i + 1, a, (a + b) // 2)
        r = build(2 * i + 2, (a + b) // 2 + 1, b)
        tree[i] = min(l, r)
    return tree[i]


# query over [l, r]
def query(i, a, b, l, r):
    if b < a:
        return INF
    elif b < l or r < a:
        return INF
    elif a >= l and b <= r:
        return tree[i]
    lhs = query(2 * i + 1, a, (a + b) // 2, l, r)
    rhs = query(2 * i + 2, (a + b) // 2 + 1, b, l, r)
    return min(lhs, rhs)


def update(i, a, b, l, r, v):
    if b < a:
        return
    elif b < l or r < a:
        return
    elif a == b:
        tree[i] += v
        return
    update(2 * i + 1, a, (a + b) // 2, l, r, v)
    update(2 * i + 2, (a + b) // 2 + 1, b, l, r, v)
    tree[i] = min(tree[2 * i + 1], tree[2 * i + 2])


if __name__ == "__main__":
    val = [randrange(1, 100) for _ in range(4)]
    n = len(val)

    build(0, 0, n - 1)
    print(val)
    print(tree[:2*n-1])
    for i in range(n):
        for j in range(i, n):
            print(i, j, query(0, 0, n-1, i, j))

    update(0, 0, n-1, 1, 3, 5)
    print("updated")
    print(tree[:2*n-1])
    for i in range(n):
        for j in range(i, n):
            print(i, j, query(0, 0, n-1, i, j))
