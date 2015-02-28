import sys
from collections import Counter


def max_toys(n):
    count = Counter()
    sale = {}
    units = 0
    n = set(n)

    for x in n:
        count[x] += 1

    for x in n:
        tmp = 0
        for i in range(5):
            tmp += count[x+i]
        sale[x] = tmp

    # print(sale)
    while True:
        tmp = 0
        tmpi = 0
        for x in sale:
            if sale[x] > tmp:
                tmp = sale[x]
                tmpi = x
        if tmp == 0:
            break
        for i in range(-1, -5, -1):
            if tmpi + i in sale:
                sale[tmpi+i] -= 1
        for i in range(5):
            if tmpi + i in sale:
                sale[tmpi+i] = 0
        units += 1
        # print(sale)

    return units


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 1:
            prices = [int(x) for x in line.split()]
            print(max_toys(prices))
