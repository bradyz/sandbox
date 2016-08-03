def binary_search(can):
    lo = 0
    hi = len(b)
    while lo < hi:
        mi = (lo + hi) // 2
        if can(b[mi]):
            hi = mi
        else:
            lo = mi + 1
    return lo


n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
r = 0
for v in a:
    x = min(binary_search(lambda t: v <= t), len(b) - 1)
    r = max(r, min(abs(v - b[x]), abs(v - b[x-1])))
print(r)
