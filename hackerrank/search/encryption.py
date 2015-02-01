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


def split_text(text):
    length = len(text)
    rows = int(floor(sqrt(length)))
    columns = int(ceil(sqrt(length)))
    grid = []
    first = 0
    last = columns
    for x in range(rows + 1):
        grid.append(text[first:last])
        first += columns
        last += columns
    return grid


def encrypt1(text, grid):
    length = len(text)
    rows = int(floor(sqrt(length)))
    columns = int(ceil(sqrt(length)))
    encryption = ""
    for i in range(columns):
        for j in range(rows + 1):
            if i < len(grid[j]):
                encryption += grid[j][i]
        encryption += " "
    return encryption


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        tmp_str = "".join(line.split())
        result = encrypt(tmp_str)
        print(result)
        grid = split_text(tmp_str)
        print(grid)
        encryption = encrypt1(tmp_str, grid)
        print(encryption)
