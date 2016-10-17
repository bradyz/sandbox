import numpy as np

# 3.1.2a, elementary matrices, transform A into B.
A = np.matrix([[1, 2, 3],
               [1, 0, 1],
               [1, -1, 1]])

B = np.matrix([[1, 0, 3],
               [1, -2, 1],
               [1, -3, 1]])

E1 = np.matrix([[1, -2, 0],
                [0, 1, 0],
                [0, 0, 1]])

print(np.array_equal(A * E1, B))

# 3.1.2b, elementary matrices, transform B into C.
B = np.matrix([[1, 0, 3],
               [1, -2, 1],
               [1, -3, 1]])

C = np.matrix([[1, 0, 3],
               [0, -2, -2],
               [1, -3, 1]])

E1 = np.matrix([[1, 0, 0],
                [-1, 1, 0],
                [0, 0, 1]])

print(np.array_equal(E1 * B, C))

# 3.1.2b, elementary matrices, transform C into I.
C = np.matrix([[1, 0, 3],
               [0, -2, -2],
               [1, -3, 1]])

E1 = np.matrix([[1, 0, 0],
                [0, 1, 0],
                [-1, 0, 1]])

E2 = np.matrix([[1, 0, 0],
                [0, -1/2, 0],
                [0, 0, 1]])

E3 = np.matrix([[1, 0, 0],
                [0, 1, 0],
                [0, 0, -1/3]])

E4 = np.matrix([[1, 0, 0],
                [0, 1, 0],
                [0, -1, 1]])

E5 = np.matrix([[1, 0, 0],
                [0, 1, 0],
                [0, 0, -3]])

E6 = np.matrix([[1, 0, -3],
                [0, 1, 0],
                [0, 0, 1]])

E7 = np.matrix([[1, 0, 0],
                [0, 1, -1],
                [0, 0, 1]])

print(E7 * E6 * E5 * E4 * E3 * E2 * E1 * C)
