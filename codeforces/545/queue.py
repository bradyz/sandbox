n = int(input())
c = list(sorted(map(int, input().split())))
r = 0
v = 0
i = 0
while i < n:
    if v <= c[i]:
        r += 1
        v += c[i]
        i += 1
    else:
        while i < n and v > c[i]:
            i += 1
print(r)
