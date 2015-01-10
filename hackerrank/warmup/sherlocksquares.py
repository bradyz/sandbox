import sys
import math


def populate_squares(top):
    top_rt = int(math.sqrt(top))
    tmp = []

    for n in range(top_rt):
        tmp.append(n * n)

    return tmp


def num_squares(in_list):
    lower = min(in_list)
    upper = max(in_list)
    count = 0
    min_sq = int(math.ceil(math.sqrt(lower)))
    while min_sq * min_sq <= upper:
        count += 1
        min_sq += 1
    return count


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = [int(x) for x in line.split()]
            print(num_squares(parsed))
