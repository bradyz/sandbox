import bisect
from random import randrange


def random_arr(cap, size):
    return [randrange(cap) for i in range(size)]


def random_sum(cap):
    return randrange(cap) + randrange(cap)


def pair_sum(arr, s):
    sorted_arr = sorted(arr)
    x = 0
    y = 0
    for n in sorted_arr:
        comp = s - n
        i = bisect.bisect_left(sorted_arr, comp)
        if i < len(sorted_arr) and sorted_arr[i] == comp:
            x = n
            y = comp
            break
    return x, y

if __name__ == "__main__":
    with open('sum-input.txt', 'r') as f:
        lines = f.readlines()
    arr = []
    s = 0
    for i, line in enumerate(lines):
        if i % 2 == 0:
            arr = [int(n) for n in line.split()]
        else:
            s = int(line.strip('\n'))
            p1, p2 = pair_sum(arr, s)
            print("Array: " + str(arr))
            print("S: " + str(s))
            if p1 and p2:
                print(str(p1) + " + " + str(p2) + " = " + str(s))
            else:
                print("No pairs found")
    max_val = 10
    cont = True
    while cont:
        arr = random_arr(max_val, 10)
        s = random_sum(max_val)
        print("Array: " + str(arr))
        print("S: " + str(s))
        p1, p2 = pair_sum(arr, s)
        if p1 and p2:
            print(str(p1) + " + " + str(p2) + " = " + str(s))
            cont = False
        else:
            print("No pairs found")
