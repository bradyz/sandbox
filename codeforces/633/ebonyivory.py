a, b, c = map(int, input().split())

x = 0
y = 0

ret = False

while a * x + b * y <= c and not ret:
    while a * x + b * y <= c and not ret:
        if a * x + b * y == c:
            ret = True
        y += 1
    x += 1
    y = 0

if ret:
    print("Yes")
else:
    print("No")
