import sys
import math


def is_possible(r, n):
    per_sector = 0
    for x in range(0, int(math.ceil(math.sqrt(r)))):
        y = math.sqrt(r - x * x)
        if math.floor(y) == y:
            per_sector += 1
    per_sector = per_sector * 4
    if per_sector <= n:
        return("possible")
    else:
        return("impossible")

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            args = line.split()
            sq_radius = int(args[0])
            num_stations = int(args[1])
            print(is_possible(sq_radius, num_stations))
