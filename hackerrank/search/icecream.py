import sys


def find_pairs(arr, s):
    contains = set()
    res = ""

    for x in range(len(arr)):
        pair = s - arr[x]
        if pair in contains:
            res += str(arr.index(pair) + 1) + " " + str(x + 1) + " "
        contains.add(arr[x])

    return res

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            num_tests = int(line.strip("\n"))
        elif i % 3 == 1:
            to_sum = int(line.strip("\n"))
        elif i % 3 == 0:
            parsed = [int(x) for x in line.split()]
            print(find_pairs(parsed, to_sum))
