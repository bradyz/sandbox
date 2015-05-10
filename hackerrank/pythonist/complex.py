from math import sqrt


def f(n):
    return "%.2f" % n


def plus(a, b):
    r0 = f(a[0] + b[0])
    r1 = f(a[1] + b[1])
    if r1 == 0:
        print(str(r0))
    else:
        if str(r1[0]) == "-":
            print(str(r0) + " - " + str(r1)[1:])
        else:
            print(str(r0) + " + " + str(r1))


def minus(a, b):
    r0 = f(a[0] - b[0])
    r1 = f(a[1] - b[1])
    if r1 == 0:
        print(str(r0))
    else:
        if str(r1[0]) == "-":
            print(str(r0) + " - " + str(r1)[1:] + "i")
        else:
            print(str(r0) + " + " + str(r1) + "i")


def times(a, b):
    r0 = f(a[0] * b[0])
    r1 = f(a[1] * b[1])
    if r1 == 0:
        print(str(r0))
    else:
        if str(r1[0]) == "-":
            print(str(r0) + " - " + str(r1)[1:] + "i")
        else:
            print(str(r0) + " + " + str(r1) + "i")


def divide(a, b):
    r0 = f(a[0] / b[0])
    r1 = f(a[1] / b[1])
    if r1 == 0:
        print(str(r0))
    else:
        if str(r1[0]) == "-":
            print(str(r0) + " - " + str(r1)[1:] + "i")
        else:
            print(str(r0) + " + " + str(r1) + "i")


def mod(a):
    print(f(sqrt(a[0]**2 + a[1]**2)))


x = list(map(int, input().split()))
y = list(map(int, input().split()))
plus(x, y)
minus(x, y)
times(x, y)
divide(x, y)
mod(x)
mod(y)
