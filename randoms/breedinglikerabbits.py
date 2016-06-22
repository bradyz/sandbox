def memo(f):
    class memo(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret
    return memo().__getitem__


@memo
def fib(n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    n2 = n // 2
    if n % 2 == 1:
        return fib(n2 - 1) + fib(n2) + 1
    return fib(n2) + fib(n2 + 1) + n2


def answer(n):
    n = int(n)
    r = None

    # evens
    lo = 0
    hi = 604462909807314587353088
    while lo + 1 < hi:
        mi = (lo + hi) // 2
        if mi % 2 != 0:
            mi -= 1
        if fib(mi) >= n:
            hi = mi
        else:
            lo = mi + 2
    mi = (lo + hi) // 2
    if mi % 2 != 0:
        mi -= 1
    if fib(mi) == n:
        r = mi

    # odds
    lo = 1
    hi = 604462909807314587353088
    while lo + 1 < hi:
        mi = (lo + hi) // 2
        if mi % 2 == 0:
            mi -= 1
        if fib(mi) >= n:
            hi = mi
        else:
            lo = mi + 1
            if lo % 2 == 0:
                lo += 1
    mi = (lo + hi) // 2
    if mi % 2 == 0:
        mi -= 1
    if fib(mi) == n:
        r = mi

    return r

print(fib(4))
print(answer(7))
