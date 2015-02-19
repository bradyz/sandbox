# Crossword Description:
# Given a grid of 1s and 0s
# 1s denote words
# 0s denote spots that are not writable
# A valid crossword is denoted by all words being connected
# Return if a crossword is valid


def is_valid(grid, rows, cols):
    def flood(r, c):
        if r >= 0 and r < rows and c >= 0 and c < cols:
            if grid[r][c] == 1 and (r, c) not in visited:
                visited.add((r, c))
                flood(r+1, c)
                flood(r-1, c)
                flood(r, c+1)
                flood(r, c-1)

    visited = set()
    has_flooded = False

    for _r in range(rows):
        for _c in range(cols):
            if has_flooded:
                if grid[_r][_c] == 1 and (_r, _c) not in visited:
                    return False
            else:
                if grid[_r][_c] == 1:
                    flood(_r, _c)
                    has_flooded = True

    return True

if __name__ == "__main__":
    num_tests = int(input())
    for test in range(num_tests):
        dim = [int(x) for x in raw_input().split()]
        my_grid = [[0 for c in range(dim[1])] for r in range(dim[0])]
        for row in range(dim[0]):
            for c, col in enumerate(raw_input()):
                my_grid[row][c] = int(col)
        is_val = is_valid(my_grid, dim[0], dim[1])
        print(is_val)
