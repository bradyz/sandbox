import numpy as np
from math import ceil, isnan

num = 0.1111111111000
num = ceil(num * 100) / 100.0

def to_shoot(d, v):
    a = np.arcsin(-9.8 * d / (v * v)) / 2
    a = np.degrees(a)
    a = -a
    a = round(a, 3)

    if a > 0:
        a = str(a)
        dot = a.index(".")
        if len(a[dot:]) != 3:
            a = a + (4 - len(a[dot:])) * "0"
    if isnan(float(a)):
        return "Impossible"
    return a

if __name__ == "__main__":
    num_tests = int(input())
    for t in range(num_tests):
        args = raw_input().split()
        dist = float(args[0])
        vel = float(args[1])
        angle = to_shoot(dist, vel)
        print(angle)
