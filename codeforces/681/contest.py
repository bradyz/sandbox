n = int(input())
r = False
for _ in range(n):
    a, b, c = input().split()
    r |= (int(b) >= 2400 and int(c) > int(b))
if r:
    print("YES")
else:
    print("NO")
