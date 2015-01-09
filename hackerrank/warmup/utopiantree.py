import sys


def height(c):
    h = 1
    x = 1

    while x <= c:
        if x % 2 != 0:
            h *= 2
        else:
            h += 1
        x += 1

    return h

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            cycles = int(line.strip('\n'))
            print(str(height(cycles)))
