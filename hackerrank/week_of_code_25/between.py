n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

factors = set()
v = b[0]
x = 1
while x * x <= v:
    if v % x == 0:
        factors.add(x)
        factors.add(v // x)
    x += 1

for v in b:
    tmp = set()
    x = 1
    while x * x <= v:
        if v % x == 0:
            tmp.add(x)
            tmp.add(v // x)
        x += 1
    values = list(factors)
    for val in values:
        if val not in tmp:
            factors.remove(val)

for v in a:
    to_remove = list()
    for val in factors:
        if val % v != 0:
            to_remove.append(val)
    for val in to_remove:
        factors.remove(val)

print(len(factors))
