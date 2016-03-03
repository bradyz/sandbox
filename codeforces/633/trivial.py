def num5(x):
    r = 0
    while x > 0:
        x //= 5
        r += x
    return r


k = int(input())
lo = 0
hi = int(1e9)

while lo < hi:
    mi = (hi + lo) // 2
    if num5(mi) < k:
        lo = mi + 1
    else:
        hi = mi

r = list()

while num5(lo) == k:
    r.append(lo)
    lo += 1

print(len(r))
if r:
    print(" ".join(map(str, r)))
