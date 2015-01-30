import sys
import copy


def has_swap(arr):
    mis = []
    swap = True
    for x in range(0, len(arr)):
        if x - 1 >= 0 and arr[x] < arr[x - 1]:
            mis.append(x)
        elif x + 1 < len(arr) and arr[x] > arr[x + 1]:
            mis.append(x)
            if len(mis) == 2 or len(mis) == 4:
                if len(mis) == 4:
                    x = mis[0]
                    y = mis[3]
                else:
                    x = mis[0]
                    y = mis[1]
                    if y - 1 >= 0 and arr[x] < arr[y - 1]:
                        swap &= False
                        if y + 1 < len(arr) and arr[x] > arr[y + 1]:
                            swap &= False
                            if x - 1 >= 0 and arr[y] < arr[x - 1]:
                                swap &= False
                                if x + 1 < len(arr) and arr[y] > arr[x + 1]:
                                    swap &= False
                                    if swap:
                                        print("yes")
                                        print("swap " + str(x + 1) + " " + str(y + 1))
                                        return True
    return False


def has_swap1(arr):
    arr_copy = copy.copy(arr)
    mis = []
    for x in range(0, len(arr)):
        if x - 1 >= 0 and arr[x] < arr[x - 1]:
            mis.append(x)
        elif x + 1 < len(arr) and arr[x] > arr[x + 1]:
            mis.append(x)
            if len(mis) == 2 or len(mis) == 4:
                if len(mis) == 4:
                    x = mis[0]
                    y = mis[3]
                else:
                    x = mis[0]
                    y = mis[1]
                    arr_copy[x], arr_copy[y] = arr_copy[y], arr_copy[x]
                    if arr_copy == sorted(arr):
                        print("yes")
                        print("swap " + str(x + 1) + " " + str(y + 1))
                        return True
    return False

def to_reverse(arr):
    mis = []
    prev = arr[0]
    run = False

    for x in range(0, len(arr)):
        cur = arr[x]
        if cur < prev:
            if not run:
                mis.append(x)
                run = True
            else:
                if run:
                    if arr[x] < arr[mis[0] - 1]:
                        return False
                if mis[0] - 2 >= 0:
                    if arr[mis[0]] > arr[x]:
                        return False
                mis.append(x)
                run = False
                prev = cur

    if len(mis) == 2:
        print("yes")
        print("reverse " + str(mis[0]) + " " + str(mis[1]))
        return True
    else:
        return False


def reverse(numbers):
    size = len(numbers)
    sorted_numbers = sorted(numbers)
    for k in range(size):
        for l in range(size):
            if k < l:
                temp = list(numbers)
                temp[k:l + 1] = reversed(temp[k:l + 1])
                print(temp)
                if temp == sorted_numbers:
                    print("yes")
                    print("reverse " + str(k + 1) + " " + str(l + 1))
                    return True
    return False

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0 and i % 2 == 1:
            parsed = [int(x) for x in line.split()]
            # res = has_swap1(parsed) or to_reverse(parsed)
            res = reverse(parsed)
            if not res:
                print("no")
