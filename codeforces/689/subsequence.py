INF = 1e9 + 1
N = 200005
tree_min = [0 for _ in range(N)]
tree_max = [0 for _ in range(N)]


# build over [a, b]
def build_min(i, a, b):
    if b < a:
        return INF
    elif a == b:
        tree_min[i] = val_b[a]
    else:
        l = build_min(2 * i + 1, a, (a + b) // 2)
        r = build_min(2 * i + 2, (a + b) // 2 + 1, b)
        tree_min[i] = min(l, r)
    return tree_min[i]


# query over [l, r]
def query_min(i, a, b, l, r):
    if b < a:
        return INF
    elif b < l or r < a:
        return INF
    elif a >= l and b <= r:
        return tree_min[i]
    lhs = query_min(2 * i + 1, a, (a + b) // 2, l, r)
    rhs = query_min(2 * i + 2, (a + b) // 2 + 1, b, l, r)
    return min(lhs, rhs)


# build over [a, b]
def build_max(i, a, b):
    if b < a:
        return -INF
    elif a == b:
        tree_max[i] = val_a[a]
    else:
        l = build_max(2 * i + 1, a, (a + b) // 2)
        r = build_max(2 * i + 2, (a + b) // 2 + 1, b)
        tree_max[i] = max(l, r)
    return tree_max[i]


# query over [l, r]
def query_max(i, a, b, l, r):
    if b < a:
        return -INF
    elif b < l or r < a:
        return -INF
    elif a >= l and b <= r:
        return tree_max[i]
    lhs = query_max(2 * i + 1, a, (a + b) // 2, l, r)
    rhs = query_max(2 * i + 2, (a + b) // 2 + 1, b, l, r)
    return max(lhs, rhs)


def binary_search_left1(i):
    lo = i
    hi = n
    while lo < hi:
        mi = (lo + hi) // 2
        if query_max(0, 0, n, i, mi) < query_min(0, 0, n, i, mi):
            lo = mi+1
        else:
            hi = mi
    return lo


def binary_search_left2(i):
    lo = i
    hi = n
    while lo < hi:
        mi = (lo + hi) // 2
        if query_max(0, 0, n, i, mi) <= query_min(0, 0, n, i, mi):
            lo = mi+1
        else:
            hi = mi
    return lo


if __name__ == "__main__":
    n = int(input())
    val_a = list(map(int, input().split()))
    val_b = list(map(int, input().split()))

    build_max(0, 0, n - 1)
    build_min(0, 0, n - 1)

    r = 0

    for i in range(n):
        print(i, query_max(0, 0, n-1, i, n))
        print(i, query_min(0, 0, n-1, i, n))
        # lower = binary_search_left1(i)
        # upper = binary_search_left2(i)
        # r += upper - lower
        # print(i, lower, upper)

    print(r)
