import sys


def quicksort1(a, s):
    p = a[0]
    less = []
    greater = []

    for x in range(s):
        if a[x] < p:
            less.append(a[x])
        elif not a[x] is p:
            greater.append(a[x])

    return less + [p] + greater


def quicksort2(a, s):
    if s == 1 or s == 0:
        if s == 0:
            return [None]
        else:
            return [a[0]]

    p = a[0]
    less = []
    greater = []

    for x in range(s):
        if a[x] < p:
            less.append(a[x])
        elif not a[x] is p:
            greater.append(a[x])

    l = quicksort2(less, len(less))
    g = quicksort2(greater, len(greater))

    if l == [None]:
        tmp = [p] + g
    elif g == [None]:
        tmp = l + [p]
    else:
        tmp = l + [p] + g

    print(" ".join(map(str, tmp)))
    return tmp


def quicksort3(aList):
    _quicksort(aList, 0, len(aList) - 1)


def _quicksort(aList, first, last):
    if first < last:
        pivot = partition(aList, first, last)
        print(" ".join(map(str, aList)))
        _quicksort(aList, first, pivot - 1)
        _quicksort(aList, pivot + 1, last)


def partition(aList, first, last):
    pivot = last - 1
    swap(aList, pivot, last)
    for i in range(first, last):
        if aList[i] <= aList[last]:
            swap(aList, i, first)
            first += 1
    swap(aList, first, last)
    return first


def swap(A, x, y):
        A[x], A[y] = A[y], A[x]

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            # a = quicksort1(parsed, size)
            # print(" ".join(map(str, a)))

            # quicksort2(parsed, size)
            quicksort3(parsed)
