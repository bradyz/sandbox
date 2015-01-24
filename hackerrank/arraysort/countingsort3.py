import sys
from collections import Counter


def countsort(arr):
    count = {}
    res = []

    for x in range(0, 100):
        count[x] = 0

    for x in arr:
        count[x] += 1

    for x in range(0, 100):
        if count[x] != 0:
            for times in range(count[x]):
                res.append(x)

    return res

if __name__ == "__main__":
    count = Counter()
    for i, line in enumerate(sys.stdin):
        if i > 0:
            args = line.split()
            num = int(args[0])
            count[num] += 1
    num_less = 0
    res = ""
    for x in range(100):
        num_less += count[x]
        res += str(num_less) + " "
    print(res)
