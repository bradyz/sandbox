import sys
from collections import Counter


def max_toys(n):
    count = Counter()
    sale = {}
    units = 0
    n = set(n)
    # print(sorted(n))

    for x in n:
        count[x] += 1

    for x in count:
        tmp = 0
        for i in range(5):
            tmp += count[x+i]
        sale[x] = tmp

    # print(sale)
    while tmp > 0:
        tmp = 0
        tmpi = 0
        for x in sale:
            if sale[x] > tmp:
                tmp = sale[x]
                tmpi = x
        if tmp == 0:
            break
        # print(tmpi)
        for i in range(5):
            if tmpi - i in sale:
                sale[tmpi-i] -= count[tmpi]
            if tmpi + i in sale:
                sale[tmpi+i] = 0
        units += 1
        # print(sale)

    return units


def max_t(n):
    arr = [0 for _ in range(10001)]
    for x in n:
        arr[x] += 1

    i = 0
    count = 0
    while(i < len(arr)):
        if arr[i] > 0:
            count += 1
            i += 4
        i += 1
    return count


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 1:
            prices = [int(x) for x in line.split()]
            print(max_t(prices))
