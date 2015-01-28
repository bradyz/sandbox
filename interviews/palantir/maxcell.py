# 1, 2, 0, 4
# 3, 0, 0, 5
# 0, 10, 0, 0
# 0, 8, 7, 6

# 1, 2, 3
# 4, 5
# 10, 8, 7, 6

grid = [[1, 2, 0, 4], [3, 0, 0, 5], [0, 0, 10, 0], [0, 8, 7, 6]]

def max_cell(g):
    def mark_adjacents(row, col):
        if g[row][col] > 0 and visited[row][col] == 0:
            visited[row][col] = 1
            ma_val = g[row][col]
            if row + 1 < num_rows:
                ma_val += mark_adjacents(row + 1, col)
            if row - 1 >= 0:
                ma_val += mark_adjacents(row - 1, col)
            if col + 1 < num_cols:
                ma_val += mark_adjacents(row, col + 1)
            if col - 1 >= 0:
                ma_val += mark_adjacents(row, col - 1)
            return ma_val
        else:
            return 0

    num_rows = len(g)
    num_cols = len(g[0])
    visited = [[0 for x in range(num_cols)] for y in range(num_rows)]
    max_c = 0

    for r in range(num_rows):
        for c in range(num_cols):
            if visited[r][c] == 0 and g[r][c] > 0:
                tmp_c = mark_adjacents(r, c)
                if tmp_c > max_c:
                    max_c = tmp_c

    return max_c

print(max_cell(grid))

# all 0s => 0
# all values => sum of grid
# 0 1 0 1
# 1 0 1 0
# 0 1 0 1 => 1
