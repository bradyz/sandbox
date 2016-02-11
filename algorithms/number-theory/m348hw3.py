import numpy as np

from matplotlib import pyplot as plt


def f1(x):
    return x ** 2 + 10 * np.cos(x)


def g1(x):
    return (-10 * np.cos(x)) ** .5 + .5


def f2(x):
    return x ** 4 - 3 * x ** 2 - 3


def g2(x):
    return (3 * x ** 2 + 3) ** .25


def f3(x):
    return x ** 3 - x - 1


def g3(x):
    print(x)
    return (x + 1) ** (1 / 3)


def f4(x):
    return np.tan(x)


def g4(x):
    return np.arctan(x) + np.pi


def fixedpoint(func, po, eps, iterations=100):
    pi = po
    for i in range(1, iterations+1):
        debug = "iteration: " + str(i)
        debug += " pi " + str(pi) + " g(pi) " + str(func(pi))
        print(debug)

        pi = func(po)
        if abs(pi - po) < eps:
            break
        po = pi
    print("pi: " + str(pi) + " g(pi): " + str(func(pi)))
    return pi


def foo(func, start, end):
    t = np.arange(start-.5, end+.5, 0.05)
    plt.plot(t, func(t), "bo")
    plt.ylim(start-.5, end+.5)
    plt.xlim(start-.5, end+.5)
    plt.plot([start, start], [end, start], "r-")
    plt.plot([start, start], [start, end], "r-")
    plt.plot([start, end], [end, end], "r-")
    plt.plot([end, end], [start, end], "r-")
    plt.plot([start, end], [start, start], "r-")
    plt.show()


if __name__ == "__main__":
    # foo(g1, 3, 4)
    # foo(g2, 1, 2)
    # foo(g3, 1, 2)
    # foo(g4, 4, 5)
    a = fixedpoint(g1, 3.6, 0, 4)
    b = (g1(a) - 0.5) ** 2 + 10 * np.cos(a)
    print(b)
