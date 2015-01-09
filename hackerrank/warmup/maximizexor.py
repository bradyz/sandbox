import sys


def maximize_xor(x, y):
    a = x
    b = y
    max_val = 0

    if a < b:
        lower = a
        upper = b
    else:
        lower = b
        upper = a

    for i in range(lower, upper + 1):
        for j in range(lower, upper + 1):
            tmp = i ^ j
            if tmp > max_val:
                max_val = tmp

    return max_val

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            x_val = int(line.strip('\n'))
        if i == 1:
            y_val = int(line.strip('\n'))
            print(str(maximize_xor(x_val, y_val)))
