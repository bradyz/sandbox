from math import sqrt

point_val = {5: 100, 10: 50, 15: 25, 20: 10}


def num_points(coordinates):
    points = 0
    for coor in coordinates:
        x = coor[0]
        y = coor[1]
        inner = sqrt(x*x+y*y)
        for dist in sorted(point_val):
            if inner <= dist:
                points += point_val[dist]
                break
    return points


num_test = int(input())

for x in range(num_test):
    shots = int(input())
    coor = []
    for y in range(shots):
        c = raw_input()
        cint = [float(xy) for xy in c.split()]
        coor.append(cint)
    points = num_points(coor)
    print(points)
