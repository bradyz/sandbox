def extended_euclid(a, b):
    """
    Solves the linear diophantine equation ax + by = d.

    All solutions are of the form -
    x = x_0 + b / d * n
    y = y_0 - a / d * n
    where n can be any integer value.
    """
    if b == 0:
        return 1, 0, a
    x, y, d = extended_euclid(b, a % b)
    return y, x - a // b * y, d


if __name__ == "__main__":
    # Want to solve: 25x + 18y = 7
    a = 25
    b = 18
    c = 7

    x, y, d = extended_euclid(a, b)

    print("a: %d b: %d, gcd: %d" % (a, b, d))
    print("x_0: %d, y_0: %d" % (x, y))

    for n in range(-5, 5):
        x1 = (x + b // d * n) * c // d
        y1 = (y - a // d * n) * c // d
        print("%d x + %d y = %d = %d" % (x1, y1, c, a * x1 + b * y1))
