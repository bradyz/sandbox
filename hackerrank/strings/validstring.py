s = list(input())
s = "".join(s)
c = dict()
for x in s:
    c[x] = c.get(x, 0) + 1
m = min(c.values())
if sum(v - m for v in c.values()) <= 1 or list(c.values()).count(1) == 1:
    print("YES")
else:
    print("NO")
