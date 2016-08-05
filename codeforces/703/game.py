x = 0
y = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    x += (a > b)
    y += (b > a)
if x > y:
    print("Mishka")
elif y > x:
    print("Chris")
else:
    print("Friendship is magic!^^")
