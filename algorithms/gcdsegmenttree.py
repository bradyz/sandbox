from random import randrange


INF = 1e9
N = 100000
tree = [0 for _ in range(N)]


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, int(a % b))


# build over [a, b]
def build(i, a, b):
    if b < a:
        return 1
    elif a == b:
        tree[i] = val[a]
    else:
        l = build(2 * i + 1, a, (a + b) // 2)
        r = build(2 * i + 2, (a + b) // 2 + 1, b)
        tree[i] = gcd(l, r)
    return tree[i]


# query over [l, r]
def query(i, a, b, l, r):
    if b < a:
        return 0
    elif b < l or r < a:
        return 0
    elif a >= l and b <= r:
        return tree[i]
    lhs = query(2 * i + 1, a, (a + b) // 2, l, r)
    rhs = query(2 * i + 2, (a + b) // 2 + 1, b, l, r)
    return gcd(lhs, rhs)


if __name__ == "__main__":
    val = [randrange(1, 100) for _ in range(4)]
    n = len(val)
    build(0, 0, n - 1)
    print(val)
    print(tree[:2*n-1])
    for i in range(n):
        for j in range(i, n):
            print(i, j, query(0, 0, n-1, i, j))
