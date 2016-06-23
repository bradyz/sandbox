n = int(input())
x = 1234567
y = 123456
z = 1234
r = False
i = 0
while i * x <= n and not r:
    j = 0
    while i * x + j * y <= n and not r:
        if (n - i * x - j * y) % z == 0:
            r = True
        j += 1
    i += 1
if r:
    print("YES")
else:
    print("NO")
