def numberToBase(n):
    if n == 0:
        return []
    return numberToBase(n // 7) + [n % 7]


n, m = map(int, input().split())
x, y = numberToBase(n), numberToBase(m)
nl, ml = len(x), len(y)
r = 0

for i in range(n):
    ni = numberToBase(i)
    ni = (nl - len(ni)) * [0] + ni
    if len(ni) != len(set(ni)):
        continue
    for j in range(m):
        mj = numberToBase(j)
        mj = (ml - len(mj)) * [0] + mj
        if len(mj) != len(set(mj)):
            continue
        if not (set(mj) & set(ni)):
            r += 1

print(r)
