import sys


def closest(arr):
    smallest = sys.maxint
    pairs = []

    for x in range(len(arr)):
        for y in range(len(arr)):
            if x != y and abs(arr[x] - arr[y]) < smallest:
                smallest = abs(arr[x] - arr[y])

    for x in range(len(arr)):
        for y in range(len(arr)):
            if x != y and abs(arr[x] - arr[y]) == smallest:
                if [arr[y], arr[x]] not in pairs:
                    pairs.append([arr[x], arr[y]])

    return pairs


def closest1(arr):
    arr.sort()
    pairs = []

    smallest = sys.maxint

    prev = arr[0]
    for x in range(1, len(arr)):
        cur = arr[x]
        if abs(cur - prev) < smallest:
            smallest = abs(cur - prev)
        prev = cur
    prev = arr[0]
    for x in range(1, len(arr)):
        cur = arr[x]
        if abs(cur - prev) == smallest:
            pairs.append(sorted([cur, prev]))
        prev = cur

    return pairs


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            total = int(line.strip("\n"))
        elif i > 0:
            parsed = [int(x) for x in line.split()]
            close = closest1(parsed)
            res = ""
            for x in close:
                for y in x:
                    res += str(y) + " "
            print(res)
