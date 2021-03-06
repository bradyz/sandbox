import sys


def countsort1(arr):
    count = {}
    res = ""

    for x in range(0, 100):
        count[x] = 0

    for x in arr:
        count[x] += 1

    for x in range(0, 100):
        res += str(count[x]) + " "

    return res


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
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            result = countsort(parsed)
            print(" ".join(map(str, result)))
