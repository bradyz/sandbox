import numpy as np

def num_waves(grid, s, e, rows, cols):
    valid = []
    num = 0
    cur = s

    while cur != e:
        if cur[0] + 1 < rows and grid[cur[0]+1] == 1:
            valid.append((cur[0]+1, cur[1]))
        if cur[0] - 1 >= 0 and grid[cur[0]+1] == 1:
            valid.append((cur[0]-1, cur[1]))
        if cur[1] + 1 < cols and grid[cur[0]+1] == 1:
            valid.append((cur[0], cur[1]+1))
        if cur[1] - 1 >= 0 and grid[cur[0]+1] == 1:
            valid.append((cur[0], cur[1]-1))

    return 0

if __name__ == "__main__":
    num_cases = int(input())
    for case in range(num_cases):
        args = [int(x) for x in raw_input().split()]
        # my_grid = [[0 for _ in range(args[1])] for _ in range(args[0])]
        my_grid = np.zeros([args[0], args[1]], int)
        for r in range(args[0]):
            row = raw_input()
            for c, val in enumerate(row):
                if val == ".":
                    my_grid[r][c] = 1
                elif val == "X":
                    my_grid[r][c] = 0
                elif val == "*":
                    my_grid[r][c] = 1
                    end = (r, c)
                elif val == "M":
                    my_grid[r][c] = 1
                    start = (r, c)
        waves = int(input())
        actual_waves = num_waves(my_grid, start, end, args[0], arg[1])
        print(my_grid)
