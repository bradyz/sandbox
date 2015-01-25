import sys
from collections import Counter


def find_median(arr):
    max_val = 0
    middle = len(arr) / 2
    i = 0
    count = Counter()

    for x in arr:
        if x > max_val:
            max_val = x
        count[x] += 1

    for x in range(max_val + 1):
        i += count[x]
        if i > middle:
            return x

    return 0

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            total = int(line.strip("\n"))
        elif i > 0:
            parsed = [int(x) for x in line.split()]
            print(find_median(parsed))
