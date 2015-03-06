def cost(n, k, c):
    c = sorted(c, reverse=True)
    p = [1 for _ in range(k)]
    m = 0
    pi = 0
    for ci in c:
        m += ci * p[pi]
        p[pi] += 1
        if pi + 1 < len(p):
            pi += 1
        else:
            pi = 0
    return m


if __name__ == "__main__":
    ri = [int(x) for x in raw_input().split()]
    n_ = ri[0]
    k_ = ri[1]
    c_ = [int(x) for x in raw_input().split()]
    print(cost(n_, k_, c_))
