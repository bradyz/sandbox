def crush(n, m, a):
    c = {}
    f = {}
    maxf = 0
    save = 0
    a = sorted(a, reverse=True)
    for val in range(1, n+1):
        c[val] = [0 for _ in range(m)]
        f[val] = 0

    for i in range(len(a)):
        for v in range(a[i][0], a[i][1]+1):
            f[v] += 1
            if f[v] > maxf:
                maxf = f[v]
                save = v

    res = 0

    for i in range(len(a)):
        if save >= a[i][0] and save <= a[i][1]:
            res += a[i][2]

    return res

if __name__ == "__main__":
    nm = [int(x) for x in raw_input().split()]
    _n = nm[0]
    _m = nm[1]
    _a = [[0 for _ in range(3)] for _ in range(_m)]

    for i in range(_m):
        bev = [long(x) for x in raw_input().split()]
        _a[i][0] = bev[0]
        _a[i][1] = bev[1]
        _a[i][2] = bev[2]

    print(crush(_n, _m, _a))
