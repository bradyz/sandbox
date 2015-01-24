import sys
from operator import itemgetter


def amount_stolen(values, slots):
    values.sort(key=itemgetter(1))
    val = 0

    for x in range(len(slots) - 1, -1, -1):
        for y in range(len(values) - 1, -1, -1):
            if values[y][0] <= slots[x]:
                val += values[y][1]
                values.pop(y)
                break

    print(val)


if __name__ == "__main__":
    tests = 0
    asdf = True
    for i, line in enumerate(sys.stdin):
        if i == 0:
            tests = int(line.strip("\n"))
        elif tests > 0:
            if asdf:
                asdf = False
                args = [int(x) for x in line.split()]
                n = args[0]  # num time slots
                k = args[1]  # items
                times = []
                items = []
            elif n > 0:
                n -= 1
                args = [int(x) for x in line.split()]
                times.append(args[1] - args[0])
            elif k > 0:
                k -= 1
                args = [int(x) for x in line.split()]
                items.append((args[0], args[1]))
                if k == 0:
                    amount_stolen(items, times)
                    asdf = True
