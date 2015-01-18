import sys

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = [int(x) for x in line.split()]
            print(sum(parsed))
