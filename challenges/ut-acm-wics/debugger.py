for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    for _ in range(k):
        b = int(input())
        r1 = 0
        lo = 0
        hi = n
        while lo < hi:
            mi = (lo + hi) // 2
            if c[mi] < b:
                lo = mi + 1
            else:
                hi = mi
        r1 = lo
        lo = 0
        hi = n
        while lo < hi:
            mi = (lo + hi) // 2
            if b < c[mi]:
                hi = mi
            else:
                lo = mi + 1
        r2 = lo
        if r1 == r2:
            print(-1)
        else:
            print(n - (r2 - r1 + 1))
