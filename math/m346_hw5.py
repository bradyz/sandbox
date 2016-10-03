import numpy as np


def ordered_bases(transformation, beta, gamma):
    """We want to find the solution to T * beta = gamma * A, where T: V -> W.

    Args:
        transformation: np.matrix of size m x n.
        beta: np.matrix of size n x n, basis for V.
        gamma: np.matrix of size m x m, basis for W.

    Returns:
        np.matrix of size m x n.
    """
    W_basis = transformation * beta
    return np.linalg.inv(gamma) * W_basis


# 2.2.2a
T = np.matrix([[2, -1],
               [3, 4],
               [1, 0]])
b = np.eye(2)
g = np.eye(3)
print("2.2.2a")
print(ordered_bases(T, b, g))

# 2.2.2b
T = np.matrix([[2, 3, 0],
               [1, 0, 1]])
b = np.eye(3)
g = np.eye(2)
print("2.2.2b")
print(ordered_bases(T, b, g))

# 2.2.2c
T = np.matrix([[2, 1, -3]])
b = np.eye(3)
g = np.eye(1)
print("2.2.2c")
print(ordered_bases(T, b, g))

# 2.2.3
T = np.matrix([[1, -1],
               [1, -0],
               [2, 1]])
b1 = np.eye(2)
b2 = np.matrix([[1, 2], [2, 3]]).T
g = np.matrix([[1, 1, 0], [0, 1, 1], [2, 2, 3]]).T
print("2.2.3")
print(ordered_bases(T, b1, g))
print(ordered_bases(T, b2, g))

# 2.2.3
A = np.matrix([[1, 3],
               [2, -1]])
B = np.matrix([[1, 0, -3],
               [4, 1, 2]])
C = np.matrix([[1, 1, 4],
               [-1, -2, 0]])
D = np.matrix([[2],
               [-2],
               [3]])
print("2.3.2a")
print(A * (2 * B + 3 * C))
print(A * B * D)
