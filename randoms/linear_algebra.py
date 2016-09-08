import math
import numpy as np


# Original.
B = np.matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

# A1 * A scales first row by 2. A * A1 scales first column by 2.
A1 = np.matrix([
    [2, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# A2 * A scales first row by 1/2. A * A2 scales first column by 1/2.
A2 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1/2, 0],
    [0, 0, 0, 1]
])

# A3 * A adds row 3 to row 1. A * A3 adds columns 3 to column 1.
A3 = np.matrix([
    [1, 0, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
])

# A4 * A swaps row 4 and row 1. A * A4 swaps columns 4 and column 1.
A4 = np.matrix([
    [0, 0, 0, 1],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 0]
])

# A5 * A subtracts row 2 from all rows except 2.
# A * A5 subtracts all columns from column 2.
A5 = np.matrix([
    [1, -1, 0, 0],
    [0, 1, 0, 0],
    [0, -1, 1, 0],
    [0, -1, 0, 1]
])

# A6 * A replaces row 4 with row 2. A * A6 adds column 4 to 3 and 0s column 4.
A6 = np.matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 0]
])

# A * A7 deletes column 1.
A7 = np.matrix([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

# Apply various transformations.
P = B * A1
Q = A2 * B * A1
R = A3 * A2 * B * A1
S = A3 * A2 * B * A1 * A4
T = A5 * A3 * A2 * B * A1 * A4
U = A5 * A3 * A2 * B * A1 * A4 * A6
V = A5 * A3 * A2 * B * A1 * A4 * A6 * A7
X = A5 * A3 * A2
Y = A1 * A4 * A6 * A7

# Show me the money.
print("Original.")
print(B)
print("Double column 1.")
print(P)
print("Halve row 3.")
print(Q)
print("Add row 3 to row 1.")
print(R)
print("Swap column 1 and 4.")
print(S)
print("Subtract row 2 from all other rows.")
print(T)
print("Replace column 4 with column 3.")
print(U)
print("Delete column 1.")
print(V)
print("X * B * Y.")
print(X * B * Y)
print("Left aggregated.")
print(X)
print("Right aggregated.")
print(Y)

# Proof on inverses.
A = np.matrix([
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
])

A = np.matrix([
    [1, 2],
    [0, 3],
])

print(A)
print(np.linalg.det(A))
print(np.linalg.inv(A))

# Proof on range space.
A = np.matrix([
    [1],
    [2],
    [3],
    [4],
])

B = np.matrix([
    [5],
    [3],
    [4],
    [-1],
])

M = A * B.T

print(M)
print(np.linalg.matrix_rank(M))

M = (B * A.T)

print(M)
print(np.linalg.matrix_rank(M))

q = np.matrix([
    [2],
    [math.sqrt(7)],
    [5],
])

I = np.identity(3)
n = np.linalg.norm(q) ** 2
print("================")
print(I - q * q.T)
print((I - q * q.T) * (I + (1 / (1 - n)) * q * q.T))
print(np.linalg.inv(I - q * q.T))
print("================")
print(q * q.T)

print(n * q * q.T)
print(q * q.T * q * q.T)
