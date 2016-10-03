import numpy as np


def mat_mul(A, B):
    A_m, A_n = len(A), len(A[0])
    B_m, B_n = len(B), len(B[0])

    assert A_n == B_m

    C = [[0 for _ in range(B_n)] for _ in range(A_m)]

    for i in range(A_m):
        for j in range(B_n):
            for k in range(A_n):
                C[i][j] += A[i][k] * B[k][j]

    return C


A = [[1, -1],
     [1, 0],
     [2, 1]]
B = [[1, 2],
     [2, 3]]
mat_mul(A, B)
