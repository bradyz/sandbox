import sys


def index_split(my_arr):
    size = len(my_arr)

    for x in range(0, size):
        if sum(my_arr[:x]) == sum(my_arr[x + 1:]):
            return "YES"

    return "NO"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            if i % 2 == 0:
                parsed = [int(x) for x in line.split()]
                print(index_split(parsed))
