X = {"R": 1, "L": -1, "U": 0, "D": 0}
Y = {"R": 0, "L": 0, "U": 1, "D": -1}

a, b = map(int, input().split())
s = input()

dx, dy = 0, 0

for c in s:
    dx += X[c]
    dy += Y[c]

ret = False

# if the robot doesnt move or endpoint is the start point
if (a == 0 and b == 0):
    ret = True

cx, cy = 0, 0

for c in s:
    cx += X[c]
    cy += Y[c]
    # dx could be 0
    k = 0
    if dx != 0 and (a - cx) % dx == 0:
        k = (a - cx) // dx
    if dy != 0 and (b - cy) % dy == 0:
        k = (b - cy) // dy
    if k >= 0 and k * dx + cx == a and k * dy + cy == b:
        ret = True
if ret:
    print("Yes")
else:
    print("No")
