import sys


def find_needle(n, h):
    return h.index(n)


def n_scan(n, h):
    for x in range(len(h)):
        if h[x] == n:
            return x
    return -1


def bin_search(n, h):
    h = sorted(h)
    first = 0
    last = len(h) - 1
    index = -1

    while first <= last and index == -1:
        mid = (first + last) / 2
        if h[mid] == n:
            index = mid
        else:
            if n < h[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return index

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            needle = int(line.strip("\n"))
        elif i == 1:
            size = int(line.strip("\n"))
        else:
            haystack = [int(x) for x in line.split()]
            print(find_needle(needle, haystack))
            print(n_scan(needle, haystack))
            print(bin_search(needle, haystack))
