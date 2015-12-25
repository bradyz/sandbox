x, y = None, None
d = None


def extendedEuclid(a, b):
    global x, y, d
    if b == 0:
        x = 1
        y = 0
        d = a
        return
    extendedEuclid(b, a % b)
    x1 = y
    y1 = x - a // b * y
    x = x1
    y = y1


if __name__ == "__main__":
    # The first solution (x0, y0) can be found using the Extended Euclid
    # algorithm shown below and the rest can be derived from
    # x = x0 + (b/d)n
    # y = y0 − (a/d)n
    # where n is an integer.
    # equation: 25x + 18y = 839
    a = 25
    b = 18

    extendedEuclid(a, b)

    print(x, y, d)

    for n in range(5):
        x1 = x + b // d * n
        y1 = y - a // d * n
        print(a * x1 + b * y1)
