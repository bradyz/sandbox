import sys


def max_noncont(arr):
    max_sum = 0
    for x in arr:
        if x > 0:
            max_sum += x
    if max_sum == 0:
        max_sum = max(arr)
    return max_sum


def max_sub(arr):
    cur_sum = 0
    max_sum = 0

    for ind in range(len(arr)):
        cur_sum += arr[ind]
        if cur_sum <= 0:
            cur_sum = 0
        if cur_sum > max_sum:
            max_sum = cur_sum
    if max_sum == 0:
        max_sum = max(arr)
    return max_sum
if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 2 == 0:
                array = [int(x) for x in line.split()]
                cont = max_sub(array)
                noncont = max_noncont(array)
                print(str(cont) + " " + str(noncont))
