from copy import deepcopy

for _ in range(int(input())):
    grid = []
    b = 0
    r = 0
    for row in range(6):
        tmp = [v for v in input()]
        grid.append(tmp)
        b += tmp.count("B")
        r += tmp.count("R")

    if r == b:
        turn = "R"
    else:
        turn = "B"

    max_score = 0
    idx = 0
    count = 0

    for c in range(6):
        tmp = deepcopy(grid)

        for r in range(5, -1, -1):
            if tmp[r][c] == ".":
                tmp[r][c] = turn
                break

        score = 0
        prev = 0

        for _c in range(7):
            for _r in range(5, -1, -1):
                if tmp[_r][_c] == turn:
                    prev += 1
                else:
                    score += prev ** 3
                    prev = 0

        score += prev ** 3

        for _r in range(6):
            for _c in range(7):
                if tmp[_r][_c] == turn:
                    prev += 1
                else:
                    score += prev ** 3
                    prev = 0

        score += prev ** 3

        if score > max_score:
            max_score = score
            idx = c
            count = 1
        elif score == max_score:
            count += 1

    if count == 1:
        for i in range(5, -1, -1):
            if grid[i][idx] == ".":
                grid[i][idx] = turn
                break
        print(turn, idx+1)
        for row in grid:
            print("".join(row))
    else:
        for i in range(5, -1, -1):
            if grid[i][0] == ".":
                grid[i][0] = turn
                break
        print(turn, 1)
        for row in grid:
            print("".join(row))
