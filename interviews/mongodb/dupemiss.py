# assume array of unique elements 1 to N
# one is duplicated, one is missing
from collections import Counter


def supposed_sum(arr):
    return (len(arr) + 1) * len(arr) / 2


def duplicated_missing(arr):
    return 0


def duplicated_missing_map(arr):
    count = Counter()

    for n in arr:
        count[n] += 1

    for x in range(1, len(arr) + 1):
        if x in count.keys():
            if count[x] == 2:
                dupe = x
            else:
                continue
        else:
            missing = x

    return dupe, missing

if __name__ == "__main__":
    with open('dupemiss-input.txt') as f:
        lines = f.readlines()

    for line in lines:
        my_arr = [int(i) for i in line.split()]
        d, m = duplicated_missing_map(my_arr)
        print(str(my_arr))
        print('Duplicated: ' + str(d) + ' Missing: ' + str(m) + '\n')
