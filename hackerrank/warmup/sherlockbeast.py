import sys


def max_decent(digits):
    res = "-1"
    for x in range(0, digits + 1):
        y = digits - x
        if x % 5 == 0 and y % 3 == 0:
            res = y * "5" + x * "3"
            break

    return int(res)


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = int(line.strip("\n"))
            print(max_decent(parsed))
