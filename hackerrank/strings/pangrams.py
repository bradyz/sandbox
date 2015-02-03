import sys
from collections import Counter


def is_pangram(string):
    count = Counter()

    for x in string:
        count[x] += 1

    if len(count.keys()) == 26:
        return "pangram"
    else:
        return "not pangram"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        parsed = line.strip().replace(" ", "").lower()
        result = is_pangram(parsed)
        print(result)
