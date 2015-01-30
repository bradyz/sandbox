import sys
# import numpy as np


def max_fence(grid, row, col):
    def valid_points(_r, _c, dr, dc):
        valid = []
        while _r < row and _r >= 0 and _c < col and _c >= 0:
            if grid[_r][_c] == 1:
                valid.append([_r, _c])
            _r += dr
            _c += dc

        return valid

    max_p = 0
    for r in range(row):
        for c in range(col):
            right_points = valid_points(r, c, 0, 1)
            for rp in right_points:
                r_dist = rp[1] - c
                down_points = valid_points(rp[0], rp[1], 1, 0)
                for dp in down_points:
                    d_dist = dp[0] - rp[0]
                    left_points = valid_points(dp[0], dp[1], 0, -1)
                    for lp in left_points:
                        l_dist = dp[1] - lp[1]
                        if l_dist + d_dist > max_p / 2:
                            up_points = valid_points(lp[0], lp[1], -1, 0)
                            for up in up_points:
                                u_dist = lp[0] - up[0]
                                if up == [r, c]:
                                    perim = r_dist + d_dist + l_dist + u_dist
                                    if perim > max_p:
                                        max_p = perim
    if max_p < 4:
        return "impossible"
    else:
        return max_p

if __name__ == "__main__":
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = line.split()
            rows = int(args[0])
            cols = int(args[1])
            my_grid = [[None for x in range(cols + 1)] for x in range(rows + 1)]
        else:
            parsed = line.strip("\n")
            for col, x in enumerate(parsed):
                if x == ".":
                    my_grid[i - 1][col] = 1
                else:
                    my_grid[i - 1][col] = 0
    print(max_fence(my_grid, rows, cols))
