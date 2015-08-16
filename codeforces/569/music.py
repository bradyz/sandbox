t, s, q = map(int, input().split())
r = 0
while s < t:
    s *= q
    r += 1
print(r)
