import numpy as np

def num_waves(grid, start, end):
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
        num_waves = int(input())
        print(my_grid)
