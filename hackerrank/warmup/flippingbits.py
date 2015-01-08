import sys


def flip_bits(el):
    return el ^ 0xffffffff

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            element = int(line.strip('\n'))
            print(str(flip_bits(element)))
