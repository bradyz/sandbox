import sys


if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = line.split()
            rows = int(args[0])
            cols = int(args[1])
            steps = int(args[2])
            my_grid = [[None for x in range(cols)] for x in range(rows)]
        else:
            parsed = [char for char in line.strip("\n").replace(" ", "")]
            for col, x in enumerate(parsed):
                my_grid[i - 1][col] = x
    print(my_grid)
