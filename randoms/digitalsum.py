from random import randrange


def foo(x):
    short = {i: dict() for i in range(10)}
    for i in range(10):
        for j in range(10):
            tmp = str(i + j)
            if len(tmp) > 1:
                short[i][j] = sum(int(x) for x in tmp)
                short[j][i] = sum(int(x) for x in tmp)
            else:
                short[i][j] = int(tmp)
                short[j][i] = int(tmp)
    cur = 0
    x = list(map(int, str(x)))
    for i in range(len(x)):
        cur = short[cur][x[i]]
    return cur


def bar(x):
    if x < 10:
        return x
    return x - 9 * int((x - 1) // 9)

for i in range(1000):
    i = randrange(int(1e100))
    if bar(i) != foo(i):
        print(bar(i), foo(i))
