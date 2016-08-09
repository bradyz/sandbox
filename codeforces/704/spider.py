n = int(input())
c = list(map(int, input().split()))
x = 0
y = 0
for v in c:
    if v != 1:
        x += v
        y += 1
    if x == 0:
        print(2)
    elif (x - y) % 2 == 0:
        print(2)
    else:
        print(1)
