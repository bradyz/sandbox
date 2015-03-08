from pprint import pprint
from random import shuffle
from copy import deepcopy


def maze_gen(row=10, col=10):
    maze = [[(x + y + 1) % (2 - y % 2) for x in range(col)] for y in range(row)]
    v = [[0 for _ in range(col)] for _ in range(row)]
    s = [(0, 0)]

    for i in range(row):
        for j in range(col):
            if maze[i][j] == 1:
                s.append((i, j))

    c = s.pop()

    while len(s) > 0:
        v[c[0]][c[1]] = 1
        neighbors = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        found = False
        shuffle(neighbors)

        for n in neighbors:
            if not found:
                if c[0] + n[0] >= 0 and c[0] + n[0] < row:
                    if c[1] + n[1] >= 0 and c[1] + n[1] < col:
                        if v[c[0]+n[0]][c[1]+n[1]] == 0:
                            wr = n[0] / 2 + c[0]
                            wc = n[1] / 2 + c[1]
                            maze[wr][wc] = 1
                            s.append((c[0]+n[0], c[1]+n[1]))
                            c = (c[0]+n[0], c[1]+n[1])
                            found = True
        if not found:
            c = s.pop()

    return maze


def solver(maze, start, end, rows, cols):
    path = [start]
    s = []
    vis = deepcopy(maze)
    cur = start

    for i in range(rows):
        for j in range(cols):
            vis[i][j] = 0

    while cur != end:
        if vis[cur[0]][cur[1]] == 0:
            path.append(cur)
            vis[cur[0]][cur[1]] = 1
            neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for n in neighbors:
                nr = cur[0] + n[0]
                nc = cur[1] + n[1]

                if nr >= 0 and nr < rows:
                    if nc >= 0 and nc < cols:
                        if vis[nr][nc] == 0 and maze[nr][nc] == 1:
                            s.append((nr, nc))
            cur = s[-1]
        else:
            cur = s.pop()
            if vis[cur[0]][cur[1]] == 1:
                path.pop()

    for p in path:
        maze[p[0]][p[1]] = 3

    return

if __name__ == "__main__":
    r, c = 11, 11
    m = maze_gen(r, c)
    solver(m, (0, 0), (r-1, c-1), r, c)
    pprint(m)
