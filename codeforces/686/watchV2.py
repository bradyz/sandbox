from itertools import permutations


def numberToBase(n):
    if n == 0:
        return []
    return numberToBase(n // 7) + [n % 7]


n, m = map(int, input().split())
x, y = numberToBase(n-1), numberToBase(m-1)
nl, ml = max(1, len(x)), max(1, len(y))
r = 0

for p in permutations("0123456", nl + ml):
    a, b = "".join(p[:nl]), "".join(p[nl:])
    r += (int(a, 7) < n and int(b, 7) < m)

print(r)
