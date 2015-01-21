import sys
import copy

count = 0


def quicksort3(aList):
    _quicksort(aList, 0, len(aList) - 1)


def _quicksort(aList, first, last):
    if first < last:
        pivot = _partition(aList, first, last)
        _quicksort(aList, first, pivot - 1)
        _quicksort(aList, pivot + 1, last)


def _partition(aList, first, last):
    global count
    for i in range(first, last):
        if aList[i] <= aList[last]:
            aList[i], aList[first] = aList[first], aList[i]
            count += 1
            first += 1
    aList[last], aList[first] = aList[first], aList[last]
    count += 1
    return first


def insertion_sort(a, s):
    count = 0
    if a == 1:
        # print_arr(a)
        return count

    for x in range(1, s):
        while x > 0 and a[x] < a[x - 1]:
            tmp = a[x]
            a[x] = a[x - 1]
            a[x - 1] = tmp
            x -= 1
            count += 1
        # print_arr(a)

    return count

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            parsed_copy = copy.copy(parsed)

            a = insertion_sort(parsed, size)
            quicksort3(parsed_copy)

            print(a - count)
