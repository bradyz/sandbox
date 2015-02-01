import sys
from collections import Counter


def missing_num(arr_a, arr_b):
    count_a = Counter()
    count_b = Counter()
    res = []

    for x in arr_a:
        count_a[x] += 1

    for x in arr_b:
        count_b[x] += 1

    for n in count_a:
        tmp = count_b[n] - count_a[n]
        if tmp > 0:
            res.append(n)

    return res

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 4 == 1:
            a_arr = [int(x) for x in line.split()]
        elif i % 4 == 3:
            b_arr = [int(x) for x in line.split()]
            missing = missing_num(a_arr, b_arr)
            print(" ".join(map(str, missing)))
