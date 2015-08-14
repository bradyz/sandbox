n, m = map(int, input().split())
c = list(input())
p = c[0]
z = 0
for v in c[1:]:
    if v == p == ".":
        z += 1
    p = v
for _ in range(m):
    x, y = input().split()
    x = int(x) - 1
    if y == "." and c[x] != ".":
        if x-1 >= 0 and c[x-1] == ".":
            z += 1
        if x+1 < n and c[x+1] == ".":
            z += 1
    elif y != "." and c[x] == ".":
        if x-1 >= 0 and c[x-1] == ".":
            z -= 1
        if x+1 < n and c[x+1] == ".":
            z -= 1
    c[x] = y
    print(z)
