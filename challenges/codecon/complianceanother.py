from collections import Counter
from itertools import permutations
o = 0
e = 0
i = input()
r = Counter(i)
for v in r.values():
    if v % 2 == 1:
        o += 1
    else:
        e += 1
if o <= 1:
    x = "".join([r[v] // 2 * v for v in r if r[v] % 2 == 0])
    print(x)
    for v in sorted(list(set(permutations(x)))):
        print(v)
    print(len(set(permutations(x))))
else:
    print(0)
