import sys

import numpy as np

for line in sys.stdin:
    A = [x.split(',') for x in line.strip().split(';')]
    A = np.array(A)

    if np.all(A.T == A):
        print('Symmetric')
    else:
        print('Not symmetric')
