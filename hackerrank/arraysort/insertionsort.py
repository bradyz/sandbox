import sys


def print_arr(arr):
    tmp = ""
    for x in arr:
        tmp += str(x) + " "
    print(tmp)
    return


def insertion_sort(a, s):
    if a == 1:
        print_arr(a)
        return

    for x in range(1, s):
        while x > 0 and a[x] < a[x - 1]:
            tmp = a[x]
            a[x] = a[x - 1]
            a[x - 1] = tmp
            x -= 1
        print_arr(a)

    return


def insertion_sort1(a, s):
    n = a[s - 1]
    is_sorted = False

    for x in range(s - 1, -1, -1):
        if not is_sorted:
            if n < a[x - 1] and x != 0:
                a[x] = a[x - 1]
            else:
                a[x] = n
                is_sorted = True
            print_arr(a)

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            size = int(line.strip("\n"))
        else:
            parsed = [int(x) for x in line.split()]
            # insertion_sort1(parsed, size)
            insertion_sort(parsed, size)
