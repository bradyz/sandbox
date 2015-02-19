# import numpy as np

def num_waves(grid, s, e, rows, cols):
    def search(r, c, visited):
        if r < rows and c < cols and r >= 0 and c >= 0 and (r, c) not in visited:
            if (r, c) == e:
                return visited
            elif grid[r][c] != 0:
                # visited.add((r, c))
                visited.append((r, c))
                tmp = search(r+1, c, visited)
                if tmp:
                    return tmp
                tmp = search(r-1, c, visited)
                if tmp:
                    return tmp
                tmp = search(r, c+1, visited)
                if tmp:
                    return tmp
                tmp = search(r, c-1, visited)
                if tmp:
                    return tmp
                visited.remove((r, c))
        else:
            return None
    vis = []
    path = search(s[0], s[1], vis)
    count = 0
    for coor in path:
        r = coor[0]
        c = coor[1]
        poss = 0
        if (r+1, c) not in path:
            if r + 1 < rows and grid[r+1][c] == 1:
                poss += 1
        if (r, c+1) not in path:
            if c + 1 < cols and grid[r][c+1] == 1:
                poss += 1
        if (r-1, c) not in path:
            if r - 1 >= 0 and grid[r-1][c] == 1:
                poss += 1
        if (r, c-1) not in path:
            if c - 1 >= 0 and grid[r][c-1] == 1:
                poss += 1
        if poss > 0:
            count += 1
    # print(grid)
    # print(path)
    return count

if __name__ == "__main__":
    num_cases = int(input())
    for case in range(num_cases):
        args = [int(x) for x in raw_input().split()]
        my_grid = [[0 for _ in range(args[1])] for _ in range(args[0])]
        # my_grid = np.zeros([args[0], args[1]], int)
        for r in range(args[0]):
            row = raw_input()
            for c, val in enumerate(row):
                if val == ".":
                    my_grid[r][c] = 1
                elif val == "X":
                    my_grid[r][c] = 0
                elif val == "*":
                    my_grid[r][c] = 9
                    end = (r, c)
                elif val == "M":
                    my_grid[r][c] = 10
                    start = (r, c)
        waves = int(input())
        actual_waves = num_waves(my_grid, start, end, args[0], args[1])
        # print(my_grid)
        # print(actual_waves)
        if actual_waves == waves:
            print("Impressed")
        else:
            print("Oops!")
