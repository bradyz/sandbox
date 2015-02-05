import sys
from collections import Counter


def replaced_num(string):
    l = len(string)
    a_str = string[:l/2]
    b_str = string[l/2:]
    a_count = Counter()
    b_count = Counter()
    to_replace = 0

    if len(a_str) != len(b_str):
        return -1

    for x in a_str:
        a_count[x] += 1

    for x in b_str:
        b_count[x] += 1

    # my_set = set(a_count.keys() + b_count.keys())
    replaced = [item for item in a_str if item not in b_str]
    to_replace = len(replaced)

    return to_replace

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i > 0:
            parsed = line.strip("\n")
            result = replaced_num(parsed)
            print(result)
