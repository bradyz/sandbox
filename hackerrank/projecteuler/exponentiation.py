for _ in range(int(input())):
    n, m = map(int, input().split())
    cache = {1: n}
    b = 1
    while b * 2 <= m:
        cache[b * 2] = cache[b] * cache[b]
        b *= 2
    tmp = m
    ret = 1
    for k in reversed(sorted(cache)):
        if tmp >= k:
            ret *= cache[k]
            tmp -= k
    print("cached values:", cache)
    print("fast:", ret)
    print("real:", n ** m)
