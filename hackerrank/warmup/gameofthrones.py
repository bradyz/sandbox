import sys
from collections import Counter


def is_palindromable(my_str):
    a = Counter()
    odds = 0

    for x in my_str:
        a[x] += 1

    for key in a.keys():
        if a[key] % 2 != 0:
            odds += 1

    if odds > 1:
        return "NO"
    else:
        return "YES"

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        given = line.strip("\n")
        print(is_palindromable(given))
