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
    max_end = 0
    max_ = 0
    for val in arr:
        max_end = max(val, max_end + val)
        max_ = max(max_, max_end)

    return max_


def ms(arr):
    def _ms(i):
        if i == -1:
            return 0
        if mem[i] != -1:
            return mem[i]
        _m = max(arr[i], mem[i-1] + arr[i])
        mem[i] = _m
        print(mem)
        return _m
    mem = [-1 for _ in range(len(arr))]
    _ms(len(arr)-1)
    return max(mem)

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 2 == 0:
                array = [int(x) for x in line.split()]
                # cont = max_sub(array)
                # noncont = max_noncont(array)
                # print(str(cont) + " " + str(noncont))
                print(array)
                print(ms(array))
