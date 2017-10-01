import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot(ax1, ax2, x, points, scores):
    ax1.clear()
    ax1.set_xlim3d(-5, 5)
    ax1.set_ylim3d(-5, 5)
    ax1.set_zlim3d(-5, 5)

    ax1.set_title('Point Visualization')

    ax1.scatter(x[0], x[1], x[2], 'r')
    ax1.scatter(points[:,0], points[:,1], points[:,2])

    ax2.set_title('Objective Function')
    ax2.plot(scores, 'r')

    plt.pause(0.01)


def sq_norm(x):
    return np.inner(x, x)


def get_objective(x, points, sq_sigma):
    score = 0.0

    for i in range(len(points)):
        score += np.exp(-1.0 / (2.0 * sq_sigma) * sq_norm(x - points[i]))

    return score


def get_gradient(x, X, sq_sigma):
    dx = np.zeros((3,))

    for i in range(len(X)):
        dx += (-1.0 / sq_sigma) * np.exp(-1.0 / (2.0 * sq_sigma) * sq_norm(x - X[i])) * (x - X[i])

    return dx


def get_hessian(x, X, sq_sigma):
    hessian = np.zeros((3, 3))

    for i in range(len(X)):
        hessian += np.outer((-1.0 / sq_sigma) * (np.exp(-1.0 / (2.0 * sq_sigma) * sq_norm(x - X[i]))), x - X[i]) + \
                (-1.0 / sq_sigma) * (np.exp(-1.0 / (2.0 * sq_sigma) * sq_norm(x - X[i]))) * np.eye(3)

    return hessian


def gradient_ascent(start, points, sq_sigma, h=1e-2):
    start += h * get_gradient(start, points, sq_sigma)

    return start


def newtons_method(start, points, sq_sigma):
    A = get_hessian(start, points, sq_sigma)
    b = -get_gradient(start, points, sq_sigma)
    x = np.linalg.solve(A, b)

    start += x

    print('Hessian condition #: %0.1f' % np.linalg.cond(A))

    return start


def main(n=50, sq_sigma=0.5):
    fig = plt.figure()

    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)

    mixture1 = 0.5 * np.random.randn(n, 3) + [0.0, 0.0, 5.0]
    mixture2 = 0.5 * np.random.randn(n, 3) + [0.0, -5.0, 0.0]
    mixture3 = 0.5 * np.random.randn(n, 3) + [5.0, 0.0, 0.0]

    points = np.concatenate((mixture1, mixture2, mixture3))

    x = np.array([4.0, 0.0, 1.0])

    scores = list()

    while True:
        scores.append(get_objective(x, points, sq_sigma))

        plot(ax1, ax2, x, points, scores)

        x = newtons_method(x, points, sq_sigma)
        # x = gradient_ascent(x, points, sq_sigma)


if __name__ == '__main__':
    np.random.seed(0)

    plt.ion()
    plt.show()

    main()
