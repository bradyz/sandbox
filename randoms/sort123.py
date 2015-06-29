c = [1, 3, 2, 3, 1, 2, 3]
n = len(c)

x, y, z = 0, 0, n-1

while y <= z:
    if c[y] == 1:
        c[x], c[y] = c[y], c[x]
        x += 1
        y += 1
    elif c[y] == 2:
        y += 1
    else:
        c[y], c[z] = c[z], c[y]
        z -= 1
    print(c)
