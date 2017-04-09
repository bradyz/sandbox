w = int(input())
n = int(input())
t = 0
for _ in range(n):
    _, y = input().split()
    t += int(y)
if t <= w:
    print("my man!")
else:
    print("uh, Rick?")
