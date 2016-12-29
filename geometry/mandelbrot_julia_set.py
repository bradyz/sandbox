from matplotlib import pyplot as plt
import numpy as np


INF = 100
MAX_ITERATIONS = 100
SLICES = 200
STEP_SIZE = 1 / SLICES
XMIN, XMAX = -2, 2
YMIN, YMAX = -1, 1

JULIA = True
JULIA_A = -0.8
JULIA_B = 0.156


# Distance from origin in complex plane.
def complex_norm_squared(a, b):
    return a ** 2 + b ** 2


# (a + bi)^2 = a^2 - b^2 + 2abi
def complex_square(a, b):
    return a * a - b * b, 2 * a * b


def iterations(a, b):
    # Want to see if a sequence diverges or converges.
    # c = a + bi.
    # f_n+1 = f_n * f_n + c.
    za, zb = a, b

    for t in range(MAX_ITERATIONS):
        # Diverges.
        if complex_norm_squared(za, zb) >= INF:
            return t

        za, zb = complex_square(za, zb)
        if JULIA:
            za, zb = za + JULIA_A, zb + JULIA_B
        else:
            za, zb = za + a, zb + b

    return MAX_ITERATIONS

if __name__ == "__main__":
    points = list()

    # Want to generate all points in complex plane.
    for a in np.arange(XMIN, XMAX, STEP_SIZE):
        for b in np.arange(YMIN, YMAX, STEP_SIZE):
            points.append((a, b, iterations(a, b)))

    # Colors are darker for more iterations.
    order = list(sorted(set(z[2] for z in points)))
    color = {z: 1 - (idx + 1) / len(order) for idx, z in enumerate(order)}

    # The Mandelbrot set is the set of all points that do not diverge.
    x = list(map(lambda z: z[0], points))
    y = list(map(lambda z: z[1], points))
    z = list(map(lambda z: color[z[2]], points))

    plt.scatter(x, y, cmap='jet', c=z, s=1, lw=0)

    plt.axis('equal')
    plt.xlim([XMIN, XMAX])
    plt.ylim([YMIN, YMAX])
    plt.show()
