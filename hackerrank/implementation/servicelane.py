import sys


def min_fit(sizes, beg, fin):
    min_val = 3
    for x in range(beg, fin + 1):
        if sizes[x] < min_val:
            min_val = sizes[x]
    return min_val

if __name__ == "__main__":
    size_arr = []
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i == 1:
                size_arr = [int(x) for x in line.split()]
            else:
                parsed = [int(x) for x in line.split()]
                start = parsed[0]
                end = parsed[1]
                print(min_fit(size_arr, start, end))
