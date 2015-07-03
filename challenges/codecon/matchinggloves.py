n = int(input())
c = {}
r = 0

for _ in range(n):
    t = input()
    if t == "".join(reversed(t)):
        continue
    if t in c:
        c[t] += 1
    else:
        c[t] = 1
    r += 1

for v in c:
    if "".join(reversed(v)) in c:
        c["".join(reversed(v))] -= c[v]
        c[v] = 0
    else:
        c[v] = -1

for v in c:
    if c[v] != 0:
        r = -1
        break
if r == -1:
    print(r)
else:
    print(r//2)
