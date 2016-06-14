def base(n, k):
    r = 0
    x = 0
    while k ** x < n:
        x += 1
    while n > 0:
        r += (10 ** x) * (n // (k ** x))
        n -= (k ** x) * (n // (k ** x))
        x -= 1
    return r


def answer(n):
    for i in range(2, 1001):
        tmp = str(base(n, i))
        if tmp == "".join(reversed(tmp)):
            return i
