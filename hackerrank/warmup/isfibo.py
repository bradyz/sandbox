import sys


def populate_fib(cap):
    tmp = [0, 1]
    index = 2
    cur = 1

    while cur < cap:
        cur = tmp[index - 1] + tmp[index - 2]
        tmp.append(cur)
        index += 1

    return tmp


def is_fib(fib_set, n):
    if n in fibs:
        return "IsFibo"
    else:
        return "IsNotFibo"


if __name__ == "__main__":
    fibs = set(populate_fib(10e10))
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = int(line.strip("\n"))
            print(is_fib(fibs, parsed))
