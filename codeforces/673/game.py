n = int(input())
c = set(map(int, input().split()))
x = 0
while x <= 90:
    f = False
    for i in range(1, 16):
        if (x + i) in c:
            x = x + i
            f = True
    if not f:
        break
print(min(90, x + 15))
