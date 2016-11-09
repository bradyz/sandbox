from math import sqrt


def xyz(color):
    d = list()
    for i in range(3, 9, 2):
        d.append(int(color[i-2:i], 16))
    return d


def func(color):
    dc = xyz(color)
    r = 0
    for i in range(len(dc)):
        r += (d[i] - dc[i]) ** 2
    return (r, color)


for _ in range(int(input())):
    n, c = input().split()
    v = [input() for _ in range(int(n))]
    d = xyz(c)
    v.sort(key=func)
    print("Case %s:" % c)
    print("\n".join(map(str, v)))
