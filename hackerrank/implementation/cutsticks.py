import sys


def print_sticks(num_arr):
    total = len(num_arr)
    num_arr.sort()
    num_zero = num_arr.count(0)

    while num_zero < total:
        min_val = num_arr[num_zero]
        tmp = 0

        print(total - num_zero)

        for x in range(num_zero, total):
            if num_arr[x] - min_val >= 0:
                num_arr[x] -= min_val
                tmp += min_val
            else:
                tmp += num_arr[x]
                num_arr[x] -= num_arr[x]

        num_zero = num_arr.count(0)

    return

if __name__ == "__main__":
    dep_map = []
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = [int(x) for x in line.split()]

    print_sticks(parsed)
