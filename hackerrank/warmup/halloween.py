import sys


def num_pieces(cuts):
    length = cuts / 2
    width = cuts - length
    return length * width


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = int(line.strip("\n"))
            print(num_pieces(parsed))
