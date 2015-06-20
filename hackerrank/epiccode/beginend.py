from collections import Counter
n = int(input())
c = Counter(input())
r = 0
for v in c.values():
    r += v * (v + 1) // 2
print(r)
