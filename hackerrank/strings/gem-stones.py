from collections import Counter
from functools import reduce


def gem_stones(rocks):
    print(len(reduce(lambda x, y: x & y, list(map(Counter, rocks)))))

if __name__ == "__main__":
    r = [input() for _ in range(int(input()))]
    gem_stones(r)
