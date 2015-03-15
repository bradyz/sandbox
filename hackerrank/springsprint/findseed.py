def populate_k(k, c, n):
    for a in range(len(k)-n-1, -1, -1):
        tmp = k[a+n]
        for b in range(0, n-1):
            tmp -= c[b] * k[a+n-b-1]
        k[a] = tmp / c[n-1]

    print(" ".join(map(str, reversed(k[:n]))))

if __name__ == "__main__":
    args = [int(x) for x in raw_input().split()]
    _n = args[0]
    _k = args[1]

    fn = [int(x) for x in raw_input().split()]
    cn = [int(x) for x in raw_input().split()]

    k = [-1 for _ in range(_k - _n + 1)] + list(reversed(fn))

    populate_k(k, cn, _n)
