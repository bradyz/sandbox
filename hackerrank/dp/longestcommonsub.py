import sys


def longest_comm(a, b, m, n):
    L = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            print(L)
            if i == 0 and j == 0:
                L[i][j] = 0
            elif a[i-1] == b[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])

    print(L)
    return L[m][n]

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = [int(x) for x in line.split()]
        elif i % 2 == 1:
            arr_a = [int(x) for x in line.split()]
        else:
            arr_b = [int(x) for x in line.split()]
            res = longest_comm(arr_a, arr_b, len(arr_a), len(arr_b))
            print(res)
