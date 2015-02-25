import sys
from copy import copy
import pprint
# import numpy as np


def longest_comm(a, b, m, n):
    L = [[[] for _ in range(n + 1)] for _ in range(m + 1)]
    # L = np.zeros([m+1, n+1], int)
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = []
            elif a[i-1] == b[j-1]:
                tmp = copy(L[i-1][j-1])
                tmp.append(a[i-1])
                L[i][j] = tmp
            else:
                if len(L[i-1][j]) > len(L[i][j-1]):
                    tmp = copy(L[i-1][j])
                    L[i][j] = tmp
                else:
                    tmp = copy(L[i][j-1])
                    L[i][j] = tmp
            pp.pprint(L)

    return L[m][n]


def lcs(a, b, m, n):
    def _lcs(i, j):
        if i == -1 or j == -1:
            return 0
        if mem[i][j] != -1:
            return mem[i][j]
        res = 0
        res = max(res, _lcs(i-1, j))
        res = max(res, _lcs(i, j-1))
        if a[i] == b[j]:
            res = max(res, _lcs(i-1, j-1)+1)
        mem[i][j] = res
        print(a[:i+1], b[:j+1])
        pp.pprint(mem)
        print("\n")
        return res
    mem = [[-1 for _ in range(n)] for _ in range(m)]
    return _lcs(m-1, n-1)

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = [int(x) for x in line.split()]
        elif i % 2 == 1:
            arr_a = [int(x) for x in line.split()]
        else:
            arr_b = [int(x) for x in line.split()]
            pp = pprint.PrettyPrinter()
            # res = longest_comm(arr_a, arr_b, len(arr_a), len(arr_b))
            # print(" ".join(map(str, res)))
            res = lcs(arr_a, arr_b, len(arr_a), len(arr_b))
            print(res)
