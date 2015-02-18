import sys
from collections import Counter


def num_to_anagram(a_str, b_str):
    a_count = Counter()
    b_count = Counter()
    num = 0

    for char in a_str:
        a_count[char] += 1

    for char in b_str:
        b_count[char] += 1

    for x in a_count.keys():
        if a_count[x] == b_count[x]:
            num += a_count[x]

    return len(a_str) - num + len(b_str) - num

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i % 2 == 0:
            a = line.strip("\n")
        else:
            b = line.strip("\n")
            num_del = num_to_anagram(a, b)
            print(num_del)
