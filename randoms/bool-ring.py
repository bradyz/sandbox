# Addition
# ===================
# plus
# 0   1   x   y
# 1   0   y   x
# x   y   0
# y   x       0
# plus1
# 0   1   x   y
# 1   0   y   x
# x   y   0   y
# y   x   y   0
# plus2
# 0   1   x   y
# 1   0   y   x
# x   y   0   1
# y   x   1   0
# plus3
# 0   1   x   y
# 1   0   x   y
# x   x   0   1
# y   y   1   0

# Multiplication
# ===================
# 0   0   0   0
# 0   1   x   y
# 0   x   x   a
# 0   y   a   y

from copy import deepcopy

r = ["0", "1", "x", "y"]
plus = {}
times = {}

for i in range(len(r)):
    plus[frozenset([r[i], "0"])] = r[i]
    plus[frozenset(r[i])] = "0"

for i in range(len(r)):
    times[frozenset([r[i], "0"])] = "0"
    times[frozenset([r[i], "1"])] = r[i]
    times[frozenset([r[i]])] = r[i]


plus[frozenset(["1", "x"])] = "y"
plus[frozenset(["1", "y"])] = "x"

plus1 = deepcopy(plus)
plus2 = deepcopy(plus)
plus3 = deepcopy(plus)

plus[frozenset(["x", "y"])] = "x"
plus1[frozenset(["x", "y"])] = "y"
plus2[frozenset(["x", "y"])] = "1"
plus3[frozenset(["x", "y"])] = "0"


def a2(_r, _p):
    for i in range(len(_r)):
        for j in range(len(_r)):
            for k in range(len(_r)):
                a = _r[i]
                b = _r[j]
                c = _r[k]
                ab = _p[frozenset([a, b])]
                bc = _p[frozenset([b, c])]
                ab_c = _p[frozenset([ab, c])]
                a_bc = _p[frozenset([a, bc])]
                if ab_c != a_bc:
                    return False
    return True

print("plus: " + str(a2(r, plus)))
print("plus1: " + str(a2(r, plus1)))
print("plus2: " + str(a2(r, plus2)))
print("plus3: " + str(a2(r, plus3)))
