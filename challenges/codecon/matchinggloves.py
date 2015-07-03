from collections import Counter
n = int(input())
c = Counter()
r = 0

for _ in range(n):
    t = input()
    if t != "".join(reversed(t)):
        c[t] += 1
        r += 1

for v in c:
    c["".join(reversed(v))] -= c[v]
    c[v] = 0

for v in c.values():
    if v != 0:
        r = -1
        break
if r == -1:
    print(r)
else:
    print(r//2)
