def is_possible(grid, row):
    grid = [[y for y in x] for x in grid]

    for r in range(row):
        grid[r].sort()

    for c in range(row):
        for r in range(1, row):
            if grid[r][c] < grid[r-1][c]:
                return "NO"

    return "YES"

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        g = []
        rows = int(input())
        for _ in range(rows):
            g.append(input())
        print(is_possible(g, rows))
