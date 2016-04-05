import numpy as np
from matplotlib import pyplot as plt


# to approximate the solution of the IVP
def euler(f, a, b, n, alpha):
    h = (b - a) / n
    t = a
    w = alpha
    yield t, w

    for i in range(1, n+1):
        w = w + h * f(t, w)
        t = a + i * h

        yield t, w


def fp(t, y):
    return 1 + y / t


def f(t):
    return t * np.log(t) + 2 * t


if __name__ == "__main__":
    plt.xlim(1, 2)
    plt.grid(True)

    domain = np.array(np.linspace(1, 2, num=100))
    plt.plot(domain, f(domain), "b-")

    tw = [(t, w) for t, w in euler(fp, 1, 2, int(1 / 0.1), 2)]
    plt.plot([x[0] for x in tw], [x[1] for x in tw], "r--")

    plt.savefig("euler_method_large.png")
    plt.show()

    plt.xlim(1, 2)
    plt.grid(True)

    plt.plot(domain, f(domain), "b-")

    tw = [(t, w) for t, w in euler(fp, 1, 2, int(1 / 0.001), 2)]
    plt.plot([x[0] for x in tw], [x[1] for x in tw], "r--")

    plt.savefig("euler_method_small.png")
    plt.show()
