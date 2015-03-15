import sys


def max_cell(g, rows, cols):
    def blob(r, c):
        result = 0
        if r < rows and r >= 0 and c < cols and c >= 0:
            if g[r][c] > 0 and v[r][c] == 0:
                v[r][c] = 1
                result += g[r][c]
                result += blob(r+1, c)
                result += blob(r-1, c)
                result += blob(r, c+1)
                result += blob(r, c-1)
                result += blob(r+1, c+1)
                result += blob(r+1, c-1)
                result += blob(r-1, c+1)
                result += blob(r-1, c-1)
        return result
    res = 0
    v = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            res = max(res, blob(i, j))
    return res


if __name__ == "__main__":
    grid = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            r = int(line)
        elif i == 1:
            c = int(line)
        else:
            grid.append([int(x) for x in line.split()])
    print(max_cell(grid, r, c))
