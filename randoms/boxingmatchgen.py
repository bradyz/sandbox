from random import random
import sys
n = int(sys.argv[1])
grid = list()
for _ in range(n):
    row = list()
    for _ in range(n):
        if random() > 0.1:
            row.append(".")
        else:
            row.append("#")
    grid.append(row)
print(n)
print("\n".join(map(lambda x: "".join(map(str, x)), grid)))
