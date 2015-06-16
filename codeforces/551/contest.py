n = int(input())
c = list(map(int, raw_input().split()))
v = dict()
r = dict()
for i in range(n):
    if c[i] in v:
        v[c[i]] += 1
    else:
        v[c[i]] = 1
        t = 1
for i in reversed(sorted(v.keys())):
    r[i] = t
    t += v[i]
print(" ".join(list(map(str, [r[c[i]] for i in xrange(n)]))))
