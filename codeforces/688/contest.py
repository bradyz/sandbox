n, d = map(int, input().split())
c = [input() for _ in range(d)]
r = 0
x = 0
for v in c:
    if "0" in v:
        x += 1
        r = max(r, x)
    else:
        x = 0
print(r)
