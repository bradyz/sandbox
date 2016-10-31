from random import random
from math import sin, cos


def backward_difference(f, x, h=0.01):
    phi_i = f(x)
    phi_j = f(x-h)
    return (phi_i - phi_j) / h


def forward_difference(f, x, h=0.01):
    phi_i = f(x+h)
    phi_j = f(x)
    return (phi_i - phi_j) / h


def central_difference(f, x, h=0.01):
    phi_i = f(x+h)
    phi_j = f(x-h)
    return (phi_i - phi_j) / (2 * h)


if __name__ == "__main__":
    x = random()

    # Find derivative of f(x) = sin(x)
    print("Evaluation of f'(x) when f(x) = sin(x) at x = %.5f" % x)
    y1 = cos(x)

    y2 = backward_difference(sin, x)
    y2_e = abs((y2 - y1) / y1)
    print("Backward difference error: %.5f" % y2_e)

    y3 = forward_difference(sin, x)
    y3_e = abs((y2 - y1) / y1)
    print("Forward difference error: %.5f" % y3_e)

    y4 = central_difference(sin, x)
    y4_e = abs((y4 - y1) / y1)
    print("Central difference error: %.5f" % y4_e)
