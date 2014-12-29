import sys


def max_val_sort(arr):
    return sorted(arr).pop()


def max_val(arr):
    max = -sys.maxint - 1
    for x in arr:
        if x > max:
            max = x
    return max

if __name__ == "__main__":
    with open('maxval-input.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        tmp = [int(i) for i in l.split()]
        print tmp
        print str(max_val(tmp))
        print str(max_val(tmp))
        print ""
