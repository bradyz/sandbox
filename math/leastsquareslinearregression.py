"""Basic algorithm for solving a least squares linear regression.

Generates random points and then tries to solve for the line that minimizes
the sum of the squares of the error.

Want to solve the optimization problem (quadratic minimization) -

min over b: sum((<x, b> - y) ** 2)

TODO: add figures for multiple dimensions (3).
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
        self.beta_hat = None

    def Train(self, x, y):
        """Adds new points to the points seen and trains the model.

        Args:
            x: (np.matrix) (n, m) shape, n samples, m dimensions.
            y: (np.matrix) (n, 1) shape, sample output.
        """
        if not self._x or not self._y:
            self._x = x
            self._y = y
        else:
            np.append(self._x, x)
            np.append(self._y, y)

    def Predict(self, x):
        """Outputs an estimation of the given points.

        Solves for coefficients with beta_hat = (((x^T)*x)^-1)*(x^T)*y.

        Args:
            x: (np.matrix) (n, m) shape, n samples, m dimensions.

        Returns:
            (np.matrix) (n, 1) shape, the predicted outputs.
        """
        n = len(self._x)
        X = np.concatenate(
                [np.matrix([[1] for _ in range(n)]), self._x[:,0]], axis=1)
        y = self._y
        self.beta_hat = np.linalg.inv(X.T * X) * X.T * y
        return x * self.beta_hat[1:, :] + self.beta_hat[0, 0]


if __name__ == "__main__":
    # Set up params.
    n = 10
    actual_slope = random.randint(-10, 10)
    actual_intercept = 0.0
    xmin = 0.0
    xmax = 100.0
    ymin = actual_intercept + xmin * actual_slope
    ymax = actual_intercept + xmax * actual_slope

    # Generate random points.
    points = list(gen(n, actual_slope, actual_intercept, xmin, xmax, beta=1.0))
    x = np.matrix([list(a[:-1]) for a in points])
    y = np.matrix([[a[1]] for a in points])

    # Do the actual regression.
    linear_regressor = LinearRegressor()
    linear_regressor.Train(x, y)

    # More params for plotting.
    predicted_y = linear_regressor.Predict(x)
    predicted_intercept = linear_regressor.beta_hat[0, 0]
    predicted_slope = linear_regressor.beta_hat[1, 0]
    predicted_ymin = predicted_intercept + predicted_slope * xmin
    predicted_ymax = predicted_intercept + predicted_slope * xmax

    # Plot points vs real line vs regression.
    fig = plt.figure()
    fig.suptitle('Least Squares Linear Regression')
    plt.plot(x, y, "ro")
    plt.plot(x, predicted_y, "bo")
    plt.plot([xmin, xmax], [ymin, ymax], "r--")
    plt.plot([xmin, xmax], [predicted_ymin, predicted_ymax], "b-")
    plt.show()
