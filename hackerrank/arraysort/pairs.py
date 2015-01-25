import sys
from collections import Counter


def num_pairs(parsed):
    count = Counter()
    num = 0

    for x in parsed:
        count[x] += 1

    for x in count:
        if count[x] > 1:
            num += count[x] * (count[x] - 1)

    return num


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0 and i % 2 == 0:
            parsed = [int(x) for x in line.split()]
            print(num_pairs(parsed))
