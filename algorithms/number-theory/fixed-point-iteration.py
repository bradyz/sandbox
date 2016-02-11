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
    return (x + 1) ** (1 / 3)


def f4(x):
    return np.tan(x)


def g4(x):
    return np.arctan(x) + np.pi


def fixedpoint(func, po, eps, iterations=100):
    pi = po

    for i in range(0, iterations+1):
        debug = "iteration: " + str(i)
        debug += "\tpi: " + str(format(pi, ".10f"))
        debug += "\tg(pi): " + str(format(func(pi), ".10f"))
        debug += "\teps: " + str(format(abs(func(po) - po), ".10f"))
        print(debug)

        pi = func(po)

        if abs(pi - po) < eps:
            break

        po = pi

    result = "Final Result\npi: " + str(format(pi, ".10f"))
    result += "\tg(pi): " + str(format(func(pi), ".10f"))
    print(result)

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
    print("Problem 1")
    p1 = fixedpoint(g1, 3.6, 0, 4)
    p1_verify = (g1(p1) - 0.5) ** 2 + 10 * np.cos(p1)
    print("f(x): " + str(p1_verify))
    print()

    print("Problem 2")
    p2 = fixedpoint(g2, 1, 1e-2)
    p2_verify = g2(p2) ** 4 - 3 * p2 ** 2 - 3
    print("f(x): " + str(p2_verify))
    print()

    print("Problem 3")
    p3 = fixedpoint(g3, 1, 1e-2)
    p3_verify = g3(p3) ** 3 - p3 - 1
    print("f(x): " + str(p3_verify))
    print()

    print("Problem 4")
    p4 = fixedpoint(g4, 4.5, 1e-5)
    p4_verify = np.tan(g4(p4) - np.pi) - p4
    print("f(x): " + str(p4_verify))
