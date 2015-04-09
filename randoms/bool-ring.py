# Addition
# ===================
# 0   1   x   y
# 1   0   y   x
# x   y   0
# y   x       0
# solution
# 0   1   x   y
# 1   0   y   x
# x   y   0   1
# y   x   1   0

# Multiplication
# ===================
# 0   0   0   0
# 0   1   x   y
# 0   x   x
# 0   y       y
# solution
# 0   0   0   0
# 0   1   x   y
# 0   x   x   0
# 0   y   0   y
# Checks validity of A2, M


class AxiomChecker:
    # _r => the list of all possible elements
    # _p => the solution of all plus operations
    @staticmethod
    def a2(_r, _p):
        for i in range(len(_r)):
            for j in range(len(_r)):
                for k in range(len(_r)):
                    a = _r[i]
                    b = _r[j]
                    c = _r[k]
                    ab = _p[frozenset([a, b])]      # (a+b)
                    bc = _p[frozenset([b, c])]      # (b+c)
                    ab_c = _p[frozenset([ab, c])]   # (a+b)+c
                    a_bc = _p[frozenset([a, bc])]   # a+(b+c)
                    if ab_c != a_bc:                # checking equality
                        return False
        return True

    # _r => the list of all possible elements
    # _t => the solution of all times operations
    # _p => the solution of all plus operations
    @staticmethod
    def md(_r, _t, _p):
        for i in range(len(r)):
            for j in range(len(r)):
                for k in range(len(r)):
                    a = _r[i]
                    b = _r[j]
                    c = _r[k]
                    bpc = _p[frozenset([b, c])]     # (b+c)
                    axb = _t[frozenset([a, b])]     # (axb)
                    axc = _t[frozenset([a, c])]     # (axc)
                    if _t[frozenset([a, bpc])] != _p[frozenset([axb, axc])]:
                        return False
        return True

# 3 Element Ring
if __name__ == "__main__":
    r = ["0", "1", "x"]
    plus = {}
    times = {}
    for i in range(len(r)):
        plus[frozenset([r[i], "0"])] = r[i]
        plus[frozenset(r[i])] = "0"

    plus[frozenset(["1"])] = "x"
    plus[frozenset(["1", "x"])] = "0"
    plus[frozenset(["x"])] = "1"

    for i in range(len(r)):
        times[frozenset([r[i], "0"])] = "0"
        times[frozenset([r[i], "1"])] = r[i]
        times[frozenset([r[i]])] = r[i]

    times[frozenset(["x"])] = "1"

    print("plus: " + str(AxiomChecker.a2(r, plus)))
    print("times: " + str(AxiomChecker.md(r, times, plus)))


# 4 Element Ring
if __name__ == "__main__":
    r = ["0", "1", "x", "y"]
    plus = {}                                       # can use sets due to A3
    times = {}

    for i in range(len(r)):
        plus[frozenset([r[i], "0"])] = r[i]         # must use frozensets due to
        plus[frozenset(r[i])] = "0"                 # mutability of sets

    plus[frozenset(["1", "x"])] = "y"
    plus[frozenset(["1", "y"])] = "x"
    plus[frozenset(["x", "y"])] = "1"

    for i in range(len(r)):
        times[frozenset([r[i], "0"])] = "0"
        times[frozenset([r[i], "1"])] = r[i]
        times[frozenset([r[i]])] = r[i]

    times[frozenset(["x", "y"])] = "0"

    print("plus: " + str(AxiomChecker.a2(r, plus)))
    print("times: " + str(AxiomChecker.md(r, times, plus)))
