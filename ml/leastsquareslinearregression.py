"""Basic algorithm for solving a least squares linear regression.

Generates random points and then tries to solve for the line that minimizes
the sum of the squares of the error.

Want to solve the optimization problem -

min over b: sum((<x, b> - y) ** 2)

TODO: add multiple dimensions.
"""

import random
import numpy as np

from matplotlib import pyplot as plt


def gen(n, a, b, xmin=0, xmax=10, beta=0.5):
    """Generator for points on a line with some error.

    Args:
        n: (int) number of points.
        a: (float) actual slope.
        b: (float) actual y intercept.
        xmin: (float) min domain of generated points.
        xmax: (float) max domain of generated points.
        beta: (float) proportional to amount of error, how messy the points are.

    Yields:
        (float tuple), x-y pairs of generated points.
    """
    for _ in range(n):
        x = xmin + (xmax-xmin) * random.random()
        y = (a * x +  b) * (1 + beta * (0.5 - random.random()))
        yield x, y


class LinearRegressor():
    """Basic least square linear regressor."""

    def __init__(self):
        self._x = None
        self._y = None

    def Train(self, x, y):
        """Adds new points to the points seen and trains the model.

        Args:
            x: (np.ndarray) (n, m) shape, n samples, m dimensions.
            y: (np.ndarray) (n,) shape, sample output.
        """
        if not self._x or self._y:
            self._x = x
            self._y = x
        else:
            np.append(self._x, x)
            np.append(self._y, y)

    def Predict(self, x):
        """Outputs an estimation of the given points.

        Solves for coefficients with beta = (((x^T)*x)^-1)*(x^T)*y.

        Args:
            x: (np.ndarray) (n, m) shape, n samples, m dimensions.

        Returns:
            (np.ndarray) (n,) shape, the predicted outputs.
        """
        result = self._x.T
        print(1, result)
        result = np.dot(result, self._x)
        print(2, result)
        result = np.linalg.inv(result)
        print(3, result)
        result = np.dot(result, self._x.T)
        print(4, result)
        result = np.dot(result, self._y)
        print(5, result)


if __name__ == "__main__":
    # Set up hyperparameter stuff.
    n = 10
    actual_slope = 1.57
    actual_intercept = 0.0
    xmin = 0.0
    xmax = 10.0
    ymin = actual_intercept + xmin * actual_slope
    ymax = actual_intercept + xmax * actual_slope

    # Generate random points.
    points = list(gen(n, actual_slope, actual_intercept, xmin, xmax))
    x = np.array([a[:-1] for a in points])
    y = np.array([a[1] for a in points])

    linear_regressor = LinearRegressor()
    linear_regressor.Train(x, y)
    linear_regressor.Predict(x)

    print(x)
    print(y)
    print(x.shape)
    print(y.shape)

    # Plot points vs real line vs regression.
    plt.plot(x, y, "ro")
    plt.plot([xmin, xmax], [ymin, ymax])
    plt.show()
