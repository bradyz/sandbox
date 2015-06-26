from collections import Counter
from math import factorial
r = Counter(input())
if sum(v % 2 == 1 for v in r.values()) <= 1:
    t = [v // 2 for v in r.values()]
    x = factorial(sum(t))
    for v in t:
        x //= factorial(v)
    print(x)
else:
    print(0)
