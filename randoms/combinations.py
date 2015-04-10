from itertools import product
n = 4
r = 3
for c in product(range(n), repeat=r):
    print(c)
