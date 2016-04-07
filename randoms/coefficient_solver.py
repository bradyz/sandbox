import numpy as np


# RS = T
# S = R^-1 T
R = np.array([[1, 1, 1, 0, 0],
              [-1, 0, 1, 1, 1],
              [1, 0, 1, -2, 2],
              [-1, 0, 1, 3, 3],
              [1, 0, 1, -3, -3]])
T = np.array([[2],
              [0],
              [2/3],
              [0],
              [2/5]])
S = np.dot(np.linalg.inv(R), T)
a, b, c, d, e = (S[i][0] for i in range(5))

for k in range(5):
    f = lambda x: x ** k
    fp = lambda x: k * x ** (k - 1)
    ret = a * f(-1) + b * f(0) + c * f(1) + d * fp(-1) + e * fp(1)
    print(ret)

print(S)
