from operator import mul
from functools import reduce

fact = lambda n: str(reduce(mul, range(1, n+1), 1))


def answer(n):
    return len(fact(n)) - len(fact(n).rstrip("0"))


def answerV2(n):
    c = 0
    for i in range(1, n+1):
        j = 1
        while 5 ** j <= n+1:
            if i % (5 ** j) == 0:
                c += 1
            j += 1
    return c

for i in range(1, 200):
    print(i, answer(i), answerV2(i))
