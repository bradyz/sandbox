def count_blobs(grid, row, col):
    blobs = 0
    visited = [[False for x in range(row)] for x in range(col)]
    for x in range(row):
        for y in range(col):
            if not visited[x][y] and grid[x][y] == 1:
                blobs += 1
                visited = mark_neighbors(grid, visited, x, y, row, col)
    return blobs


def mark_neighbors(grid, vis, x, y, row, col):
    if not vis[x][y]:
        vis[x][y] = True
        if grid[x][y] == 1:
            if x + 1 < row:
                vis = mark_neighbors(grid, vis, x + 1, y, row, col)
            if x - 1 >= 0:
                vis = mark_neighbors(grid, vis, x - 1, y, row, col)
            if y + 1 < col:
                vis = mark_neighbors(grid, vis, x, y + 1, row, col)
            if y - 1 >= 0:
                vis = mark_neighbors(grid, vis, x, y - 1, row, col)
    return vis


def parse_grid(line_arr, num_rows, start):
    tmp_arr = []
    for x in range(start, start + num_rows):
        line = line_arr[x]
        tmp_arr.append([int(i) for i in line.split()])
    return tmp_arr


def parse_dim(line_arr, start):
    row = int(line_arr[start + 0].strip('\n'))
    col = int(line_arr[start + 1].strip('\n'))
    return row, col


if __name__ == "__main__":
    with open('countblobs-input.txt', 'r') as f:
        lines = f.readlines()
    cur = 0
    while cur < len(lines):
        row, col = parse_dim(lines, cur)
        cur += 2
        tmp_grid = parse_grid(lines, row, cur)
        cur += row
        blobs = count_blobs(tmp_grid, row, col)
        for r in tmp_grid:
            print(r)
        print("num_blobs: " + str(blobs) + "\n")
