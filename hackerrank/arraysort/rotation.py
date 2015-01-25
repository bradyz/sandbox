import sys


def index_rotate(arr, num_rot, index):
    num_rot %= len(arr)
    if num_rot > index:
        return arr[len(arr) - num_rot + index]
    else:
        return arr[index - num_rot]


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = line.split()
            rot = int(args[1])
        elif i == 1:
            parsed = [int(x) for x in line.split()]
        elif i > 1:
            num = int(line.strip("\n"))
            print(index_rotate(parsed, rot, num))
