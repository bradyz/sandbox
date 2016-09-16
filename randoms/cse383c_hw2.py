import math
import numpy as np


# 3.3.a
x = np.matrix([
    [1],
    [0],
    [0],
])

n = np.linalg.norm(x, np.inf)
m = np.linalg.norm(x, 2)
print("3.3.a", n, m)

# 3.3.b
x = np.matrix([
    [1],
    [1],
    [1],
])

n = np.linalg.norm(x, 2)
m = math.sqrt(3) * np.linalg.norm(x, np.inf)
print("3.3.b", n, m)

# 3.3.c
A = np.matrix([
    [1, 1],
    [0, 0],
    [0, 0],
])

# inf norm of a matrix is max sum of absolute value of row
n = np.linalg.norm(A, np.inf)
m = math.sqrt(2) * np.linalg.norm(A, 2)
print("3.3.c", n, m)

# 3.3.d
A = np.matrix([
    [1, 0],
    [1, 0],
    [1, 0],
])

n = np.linalg.norm(A, 2)
m = math.sqrt(3) * np.linalg.norm(A, np.inf)
print("3.3.d", n, m)

# 3.4
A = np.matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
])

# Deletes one row.
C = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
])

# Deletes one column.
D = np.matrix([
    [0, 0],
    [1, 0],
    [0, 1],
])

# (3 x 4) (4 x 3) (3 x 2)
print(3.4)
# Norm of deletion matrices is 1.
print(np.linalg.norm(C, 2), np.linalg.norm(D, 2))
# Norm of "submatrix" of A is less than A. See Theorem 3.14.
print(np.linalg.norm(C * A * D, np.inf), np.linalg.norm(A, np.inf))
print(A)
print(C * A)
print(C * A * D)
print(A * D)
