import sys
import itertools
from collections import Counter


def max_pair(g_list):
    val_freq = Counter()
    max_val = 0
    max_freq = 0

    for subset in itertools.combinations(g_list, 2):
        a = subset[0]
        b = subset[1]
        c = 0
        length = min(len(a), len(b))
        for i in range(length):
            if a[i] == '1' or b[i] == '1':
                c += 1
        val_freq[c] += 1

    max_val = max(val_freq.keys())
    max_freq = val_freq[max_val]

    return max_val, max_freq

if __name__ == "__main__":
    given_list = []
    for i, line in enumerate(sys.stdin):
        if i > 0:
            given = line.strip("\n")
            given_list.append(given)
    num, count = max_pair(given_list)
    print(num)
    print(count)
