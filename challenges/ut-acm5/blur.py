for _ in range(int(input())):
    args = [int(v) for v in input().split()]
    n = args[0]
    m = args[1]
    k = args[2]
    b = 2 * args[2] + 1
    grid = []

    for __ in range(n):
        grid.append([int(v) for v in input().split()])

    new_grid = []

    for i in range(n):
        new_row = []
        for j in range(m):
            av = 0
            for x in range(-k, k+1):
                for y in range(-k, k+1):
                    if i+x >= 0 and i+x < n and j+y >= 0 and j+y < m:
                        av += grid[i+x][j+y]
            av /= b*b
            new_row.append(round(av))
        new_grid.append(new_row)

    for row in new_grid:
        print(" ".join(map(str, row)))
