# Permutations Descriptions:
# Return all possible permutations of a string


import sys


def permutations(a_string):
    arr = list(a_string)
    for x in range(len(arr)):
        for y in _permutations(arr[x], arr[:x] + arr[x+1:]):
            yield y


def _permutations(prefix, arr):
    if len(arr) == 0:
        yield prefix

    for x in range(len(arr)):
        for y in _permutations(prefix + arr[x], arr[:x] + arr[x+1:]):
            yield y


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        a_str = line.strip("\n")
        a = permutations(a_str)
        for perm in a:
            print(perm)
