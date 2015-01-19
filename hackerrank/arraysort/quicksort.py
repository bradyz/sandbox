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

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            a = quicksort1(parsed, size)
            print(" ".join(map(str, a)))
