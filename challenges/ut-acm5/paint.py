for _ in range(int(input())):
    args = [int(v) for v in input().split()]
    n = args[0]
    m = args[1]
    q = args[2]

    grid = []

    for row in range(n):
        grid.append([v for v in input()])

    for __ in range(q):
        query = [v for v in input().split()]
        vis = [[False for _ in range(m)] for _ in range(n)]
        color = grid[int(query[0])][int(query[1])]

        def flood(r, c):
            if r < n and c < m and r >= 0 and c >= 0 and not vis[r][c]:
                if grid[r][c] == color:
                    vis[r][c] = True
                    grid[r][c] = query[2]
                    flood(r+1, c)
                    flood(r-1, c)
                    flood(r, c+1)
                    flood(r, c-1)

        flood(int(query[0]), int(query[1]))

    for row in grid:
        print("".join(map(str, row)))
