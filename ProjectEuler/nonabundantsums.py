def factors(x):
    i = 2
    r = set([1])
    while i * i <= x:
        if x % i == 0:
            r.add(i)
            r.add(x // i)
        i += 1
    return r

a = list()
for i in range(2, 28124):
    if sum(factors(i)) > i:
        a.append(i)
n = len(a)
c = set(range(1, 28124))
for i in range(n):
    x = a[i]
    for j in range(i, n):
        y = a[j]
        s = x + y
        if s in c:
            c.remove(s)
print(sum(c))
