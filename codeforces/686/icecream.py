n, x = map(int, input().split())
r = 0
for _ in range(n):
    a, b = input().split()
    if a == "+":
        x += int(b)
    else:
        if int(b) <= x:
            x -= int(b)
        else:
            r += 1
print(x, r)
