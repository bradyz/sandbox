import numpy as np
import matplotlib.pyplot as plt


def score(x, w, b):
    return np.dot(x, w) + b


def plot_random(n=50):
    for _ in range(n):
        x = (np.random.rand(2) - 0.5) * 2.0

        if score(x, w, b) > 0:
            plt.plot(x[0], x[1], 'r.')
        else:
            plt.plot(x[0], x[1], 'b.')


def plot_plane():
    ys = np.array([-1.0, 1.0])
    xs = (-b - w[1] * ys) / w[0]

    plt.plot(xs, ys, 'c--')


def plot():
    plt.axis('equal')
    plt.xlim([-1, 1])
    plt.ylim([-1, 1])
    plt.arrow(0, 0, w_hat[0], w_hat[1])
    plt.plot(u[0], u[1], '+')
    plt.plot(v[0], v[1], 'o')
    plot_plane()
    plot_random()


np.random.seed(0)

u = np.random.rand(2)
v = np.random.rand(2)

w = u - v
w_hat = w / np.linalg.norm(w)

b = -np.dot(w, (u + v) / 2.0)

plt.subplot(3, 1, 1)
plot()

b = 0.5

plt.subplot(3, 1, 2)
plot()

b = 1.0

plt.subplot(3, 1, 3)
plot()

plt.show()
