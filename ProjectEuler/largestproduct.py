import sys
from functools import reduce

g = [list(map(int, line.split())) for line in sys.stdin]
n = len(g)
m = 0

for i in range(n-4):
    for j in range(n):
        m = max(m, reduce(lambda x, y: x * y, [g[i+z][j] for z in range(4)]))

for i in range(n):
    for j in range(n-4):
        m = max(m, reduce(lambda x, y: x * y, [g[i][j+z] for z in range(4)]))

for i in range(n-4):
    for j in range(n-4):
        m = max(m, reduce(lambda x, y: x * y, [g[i+z][j+z] for z in range(4)]))

for i in range(n-4):
    for j in range(3, n):
        m = max(m, reduce(lambda x, y: x * y, [g[i+z][j-z] for z in range(4)]))

print(m)
