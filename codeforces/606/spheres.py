val1 = list(map(int, input().split()))
val2 = list(map(int, input().split()))
z = 0
for x, X in zip(val1, val2):
    if x > X:
        z += (x - X) // 2
    else:
        z += x - X
if z >= 0:
    print("Yes")
else:
    print("No")
