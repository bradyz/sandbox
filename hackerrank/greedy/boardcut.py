def board(mc, nc):
    m = len(mc)
    n = len(nc)
    mc = sorted(mc, reverse=True)
    nc = sorted(nc, reverse=True)
    c = 0
    l = 1
    w = 1

    while l <= m or w <= n:
        if l-1 == m:
            c += nc[w-1]*l
            w += 1
        elif w-1 == n:
            c += mc[l-1]*w
            l += 1
        elif mc[l-1] > nc[w-1]:
            c += mc[l-1]*w
            l += 1
        else:
            c += nc[w-1]*l
            w += 1

    return c % 1000000007


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        _d = [long(x) for x in raw_input().split()]
        _mc = [long(x) for x in raw_input().split()]
        _nc = [long(x) for x in raw_input().split()]
        print(board(_mc, _nc))
