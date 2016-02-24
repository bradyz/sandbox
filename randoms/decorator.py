from time import time


def memo_decorate(func):
    cache = dict()

    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return wrapper


@memo_decorate
def fib_decorated(x):
    if x <= 2:
        return 1
    return fib_decorated(x-1) + fib_decorated(x-2)


def fib_undecorated(x):
    if x <= 2:
        return 1
    return fib_undecorated(x-1) + fib_undecorated(x-2)


if __name__ == "__main__":
    n = 40

    s = time()
    fib_undecorated(n)
    print("normal:", time() - s)

    s = time()
    fib_decorated(n)
    print("memoed:", time() - s)
