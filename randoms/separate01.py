# Separate 0s and 01s Description:
# Given a 1d array of random 0s and 1s
# Return an array with all the 0s on the left
# And all the 1s on the right

from Queue import Queue

def separated(arr):
    return sorted(arr)


def queue_separated(arr):
    z_i = Queue()

    for i, val in enumerate(arr):
        if val == 1:
            z_i.put(i)
        else:
            tmp_i = z_i.get()
            z_i.put(i)
            arr[i], arr[tmp_i] = arr[tmp_i], arr[i]

    return arr


def is_valid(arr):
    if len(arr) == 0:
        return True

    prev = arr[0]

    for cur in arr:
        if cur is not arr[0]:
            if cur == 0 and prev == 1:
                return False
        prev = cur

    return True


if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        my_arr = [int(val) for val in raw_input().split()]
        res_arr = queue_separated(my_arr)
        print(res_arr)
