import sys
from collections import Counter


def max_wishes(my_arr, num_row, num_col):
    to_flip = []
    count = Counter()

    for x in range(num_row):
        o_count = 0
        z_count = 0
        for y in range(num_col):
            if my_arr[x][y] == 1:
                o_count += 1
            else:
                z_count += 1
        if o_count > z_count:
            tmp_list = [i for i, t in enumerate(my_arr[x]) if t == 0]
            for a in tmp_list:
                count[a] += 1
        else:
            tmp_list = [i for i, t in enumerate(my_arr[x]) if t == 1]
            for a in tmp_list:
                count[a] += 1
        to_flip.append(tmp_list)

    counter = Counter()
    for x in to_flip:
        counter[str(x)] += 1

    max_len = 0
    for x in counter.keys():
        if counter[str(x)] > max_len:
            max_len = counter[str(x)]

    return max_len


def change_letters(my_arr, num_col, num_row):
    for x in range(num_col):
        for y in range(num_row):
            if my_arr[x][y] == "T":
                my_arr[x][y] = 1
            else:
                my_arr[x][y] = 0

    return my_arr

if __name__ == "__main__":
    letters = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            parsed = [int(x) for x in line.split()]
            col = parsed[0]
            row = parsed[1]
        else:
            parsed = [str(x) for x in line.strip("\n")]
            letters.append(parsed)

    temp = change_letters(letters, col, row)
    print(max_wishes(letters, col, row))
