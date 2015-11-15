from math import atan2, pi
angles = list()
for i in range(int(input())):
    x, y = map(int, input().split())
    angle = atan2(y, x)
    angles.append((angle, i+1))
    angles.append((angle+2*pi, i+1))
    print(i+1, angle, angle+2*pi)
angles.sort()
a = angles[0][1]
b = angles[1][1]
for i in range(1, len(angles)):
    print("best:", abs(angles[a][0]-angles[b][0]), angles[a][1], angles[b][1])
    if abs(angles[i][0]-angles[i-1][0]) < abs(angles[a][0]-angles[b][0]):
        print("newb:", abs(angles[i][0]-angles[i-1][0]), angles[i][1], angles[i-1][1])
        a = i
        b = i-1
print(angles[a][1], angles[b][1])
