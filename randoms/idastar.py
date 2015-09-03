from sys import maxsize as MAXINT
from mazegen import maze_gen
from pprint import PrettyPrinter


def h(x, y):
    return abs(n-1-x) + abs(m-1-y)


def idastar():
    def dfs(x, y, c):
        if x < 0 or y < 0 or x >= n or y >= m or g[x][y] == 0 or \
                h(x, y) + c > limit:
            return [], MAXINT

        if x == n-1 and y == m-1:
            return [(x, y)], c

        min_u = []
        min_v = MAXINT

        for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            if (x+i, y+j) in p:
                continue

            p[(x+i, y+j)] = (x, y)
            u, v = dfs(x+i, y+j, c+1)

            if v < min_v:
                min_u = u
                min_v = v

        if min_u:
            return [(x, y)] + min_u, min_v

        return [], MAXINT

    limit = 1

    path = []
    cost = -1

    while not path:
        p = {(0, 0): None}
        path, cost = dfs(0, 0, 0)
        limit += 1
        print("increasing f limit to " + str(limit))

    return path, cost

if __name__ == "__main__":
    n, m = 20, 20
    g = maze_gen(n, m)
    n, m = len(g), len(g[0])

    pp = PrettyPrinter()
    pp.pprint(g)

    solution, cost = idastar()

    # for x, y in solution:
    #     g[x][y] = 2

    pp = PrettyPrinter()
    pp.pprint(g)

    print(solution)
    print(cost)
