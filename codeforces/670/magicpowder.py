def can(x):
    k1 = k
    for ai, bi in zip(a, b):
        if bi + k1 < ai * x:
            return False
        k1 -= max(0, ai * x - bi)
    return True

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

r = -1
lo = 0
hi = 2001

while lo < hi:
    mi = (lo + hi) // 2

    if can(mi):
        r = max(r, mi)
        lo = mi + 1
    else:
        hi = mi

print(r)
