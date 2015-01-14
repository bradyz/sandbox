import sys


def index_split(my_arr):
    size = len(my_arr)

    for x in range(0, size):
        if sum(my_arr[:x]) == sum(my_arr[x + 1:]):
            return "YES"

    return "NO"


def improved_index(my_arr):
    sum_arr = []

    for x in range(len(my_arr)):
        if x == 0:
            sum_arr.append(my_arr[x])
        else:
            sum_arr.append(my_arr[x] + sum_arr[x - 1])

    right_sum = 0
    count = 0

    for x in range(len(my_arr) - 1, -1, -1):
        if x == 0:
            if right_sum == 0:
                count += 1
        elif x == len(my_arr) - 1:
            if sum_arr[x - 1] == 0:
                count += 1
            right_sum += my_arr[x]
        else:
            if right_sum == sum_arr[x - 1]:
                count += 1
            right_sum += my_arr[x]

    if count > 0:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 2 == 0:
                parsed = [int(x) for x in line.split()]
                print(improved_index(parsed))
