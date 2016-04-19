from math import exp, log, e

import numpy as np
from matplotlib import pyplot as plt


def rk(f, a, b, alpha, n):
    h = (b - a) / n
    t = a
    w = alpha

    yield t, w

    for i in range(1, n+1):
        k1 = h * f(t, w)
        k2 = h * f(t + h / 2, w + k1 / 2)
        k3 = h * f(t + h / 2, w + k2 / 2)
        k4 = h * f(t + h, w + k3)

        w = w + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t = a + i * h

        yield t, w


def deri1(t, y):
    return np.exp(t - y)


def func1(t):
    return np.log(np.exp(t) + e - 1)


if __name__ == "__main__":
    yt = rk(deri1, 0, 1, 1, int(1 / 0.01))

    plt.grid(True)

    domain = np.array(np.linspace(0, 1, num=100))
    plt.plot(domain, func1(domain), "b-")

    tw = [(t, w) for t, w in yt]
    print("\n".join(map(str, tw)))
    plt.plot([x[0] for x in tw], [x[1] for x in tw], "r+--")

    plt.savefig("runge_kutta.png")

    plt.show()
