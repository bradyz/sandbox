def crush(n, m, a):
    va = []
    for tri in a:
        va.append([tri[0], tri[2]])
        va.append([tri[1]+1, -tri[2]])
    va.sort()
    curv = 0
    maxv = 0
    for i in range(m * 2):
        curv += va[i][1]
        maxv = max(maxv, curv)
    return maxv

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
