def binary_search_left(start):
    lo = start
    hi = n + 1
    while lo < hi:
        mi = (lo + hi) // 2
        if enough(start, mi):
            hi = mi
        else:
            lo = mi + 1
    return lo


def enough(lo, hi):
    x = dict(c[hi])
    for k, v in c[lo].items():
        x[k] -= v
        if x[k] == 0:
            x.pop(k)
    return (set(x.keys()) == a)


n = int(input())
s = input()
a = set(s)
c = [dict() for _ in range(n+1)]
for i in range(1, n+1):
    c[i] = dict(c[i-1])
    c[i][s[i-1]] = c[i].get(s[i-1], 0) + 1
r = int(1e9)
for i in range(n+1):
    x = binary_search_left(i)
    if x < n + 1:
        r = min(r, x - i)
print(r)
