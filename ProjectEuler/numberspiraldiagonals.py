r = 1
for l in range(3, 1002, 2):
    s = (l - 2) ** 2 + 1
    r += (s + l - 2)
    r += (s + l - 3 + l)
    r += (s + l - 4 + l + l)
    r += (s + l - 5 + l + l + l)
print(r)
