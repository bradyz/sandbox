from math import exp, log, e

import numpy as np
from matplotlib import pyplot as plt


def rkf(f, a, b, alpha, tol, hmin, hmax):
    t = a
    w = alpha
    h = hmax
    flag = 1

    yield t, w

    while flag == 1:
        k1 = h*f(t, w)
        k2 = h*f(t+1/4*h, w + 1 / 4 * k1)
        k3 = h*f(t+3/8*h, w + 3 / 32 * k1 + 9 / 32 * k2)
        k4 = h*f(t+12/13*h, w + 1932/2197*k1 - 7200/2197*k2 + 7296/2197*k3)
        k5 = h*f(t+h, w + 439/216*k1 - 8*k2 + 3680/513*k3 - 845/4104*k4)
        k6 = h*f(t+1/2*h, w-8/27*k1 + 2*k2 - 3544/2565*k3 + 1859/4104*k4 - 11/40*k5)
        r = 1/h * abs(1/360*k1 - 128/4275*k3 - 2197/75240*k4 + 1/50*k5 + 2/55*k6)
        if r < tol:
            t = t + h
            w = w + 25/216*k1 + 1408/2565*k3 + 2197/4104*k4 - 1/5*k5
            yield t, w
        d = 0.84 * (tol / r) ** .25
        if d <= 0.1:
            h = 0.1*h
        elif d >= 4:
            h = 4*h
        else:
            h = d*h
        if h > hmax:
            h = hmax
        if t >= b:
            flag = 0
        elif t + h > b:
            h = b - t
        elif h < hmin:
            flag = 0
            print("min h exceeded")


def deri1(t, y):
    return np.exp(t - y)


def func1(t):
    return np.log(np.exp(t) + e - 1)


if __name__ == "__main__":
    yt = rkf(deri1, 0, 1, 1, 1e-4, 0.005, 0.025)

    plt.grid(True)

    domain = np.array(np.linspace(0, 1, num=100))
    plt.plot(domain, func1(domain), "b-")

    tw = [(t, w) for t, w in yt]
    plt.plot([x[0] for x in tw], [x[1] for x in tw], "r+--")

    plt.savefig("runge_kutta_fehlberg.png")

    plt.show()
