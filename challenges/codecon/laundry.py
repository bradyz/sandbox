from collections import Counter
import sys

c = Counter([line.strip("\n") for line in sys.stdin])
for v in sorted(c):
    if v.count("sock") > 0:
        if c[v] > 1:
            print(str(c[v]//2) + "|" + v)
        if c[v] % 2 == 1:
            print("0|" + v)
    else:
        print(str(c[v]) + "|" + v)
