def extendedEuclid(a, b):
    global x, y, d
    if b == 0:
        x = 1
        y = 0
        d = a
        return

    extendedEuclid(b, a % b)
    x1 = y
    y1 = x - (a // b) * y
    x = x1
    y = y1


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    x = 0
    y = 0
    d = 0
