import sys
from math import floor, ceil, sqrt


def encrypt(a_str):
    a = list(a_str)
    l = len(a_str)
    rows = int(floor(sqrt(l)))
    cols = int(ceil(sqrt(l)))
    res = ""

    for c in range(cols):
        for r in range(rows + 1):
            if r * cols + c < l:
                res += str(a[r * cols + c])
        res += " "

    return res


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        tmp_str = "".join(line.split())
        result = encrypt(tmp_str)
        print(result)
