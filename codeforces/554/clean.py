from collections import Counter
n = int(input())
c = Counter(tuple(tuple(input()) for _ in range(n)))
x = Counter()
for v in c:
    r = tuple(i for i in range(n) if v[i] == '0')
    x[r] += c[v]
print(max(x.values()))
