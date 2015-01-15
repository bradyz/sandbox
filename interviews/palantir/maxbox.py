import sys
import copy


def flip_col(arr, r, c, col_num):
    tmp_arr = copy.deepcopy(arr)
    for x in range(r):
        if tmp_arr[x][col_num] == 1:
            tmp_arr[x][col_num] = 0
        else:
            tmp_arr[x][col_num] = 1
    return tmp_arr


def max_wishes(my_arr, num_row, num_col):
    max_num = 0

    tmp_score = 0
    for x in range(num_row):
        if sum(my_arr[x]) == 1 or sum(my_arr[x]) == 0:
            tmp_score += 1

    max_num = tmp_score

    for x in range(num_col):
        tmp = flip_col(my_arr, num_row, num_col, x)
        tmp_score = 0
        for x in range(num_row):
            if sum(tmp[x]) == 1 or sum(tmp[x]) == 0:
                tmp_score += 1
        if tmp_score > max_num:
            max_num = tmp_score

    return max_num


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
