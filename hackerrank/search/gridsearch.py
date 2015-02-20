# import numpy as np


def contains_needle(hay, needle, h_row, h_col, n_row, n_col):
    # print(hay)
    # print(needle)
    for _r in range(h_row-n_row+1):
        for _c in range(h_col-n_col+1):
            cont = True
            n_r = 0
            while cont and n_r < n_row:
                n_c = 0
                while cont and n_c < n_col:
                    if hay[_r+n_r][_c+n_c] != needle[n_r][n_c]:
                        cont = False
                    n_c += 1
                n_r += 1
            if cont:
                return True
    return False

if __name__ == "__main__":
    num_tests = int(input())

    for test in range(num_tests):
        block_dim = [int(x) for x in raw_input().split()]
        row = block_dim[0]
        col = block_dim[1]
        my_grid = [[0 for c in range(col)] for r in range(row)]
        # my_grid = np.zeros([row, col], int)
        for r in range(row):
            my_row = [int(x) for x in raw_input()]
            for c in range(col):
                my_grid[r][c] = my_row[c]
        find_dim = [int(x) for x in raw_input().split()]
        find_row = find_dim[0]
        find_col = find_dim[1]
        my_block = [[0 for fc in range(find_col)] for fw in range(find_row)]
        # my_block = np.zeros([find_row, find_col], int)
        for r in range(find_row):
            tmp_row = [int(x) for x in raw_input()]
            for c in range(find_col):
                my_block[r][c] = tmp_row[c]
        found = contains_needle(my_grid, my_block, row, col, find_row, find_col)
        print(found)
