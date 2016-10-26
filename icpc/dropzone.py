from queue import Queue


def sources(grid, m, n):
    result = set()
    for i in range(m):
        result.add((i, 0))
        result.add((i, n-1))
    for i in range(n):
        result.add((0, i))
        result.add((m-1, i))
    return result


def sinks(grid, m, n):
    result = set()
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "D":
                result.add((i, j))
    return result


def residual(grid, m, n):
    res = dict()
    for x in range(m):
        for y in range(n):
            if grid[x][y] == "X":
                continue
            res[(x, y)] = dict()
    for x in range(m):
        for y in range(n):
            if grid[x][y] == "X":
                continue
            for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                elif grid[nx][ny] == "X":
                    continue
                res[(x, y)][(nx, ny)] = 1
                res[(nx, ny)][(x, y)] = 1
    return res


def bfs(grid, m, n, source, sink, parent, residual):
    q = Queue()
    for x, y in source:
        q.put((x, y))
        parent[(x, y)] = "source"
    while not q.empty():
        x, y = q.get()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            elif (nx, ny) in parent:
                continue
            elif grid[nx][ny] == "X":
                continue
            elif residual[(x, y)][(nx, ny)] <= 0:
                continue
            parent[(nx, ny)] = (x, y)
            if (nx, ny) in sink:
                parent["sink"] = (nx, ny)
            else:
                q.put((nx, ny))
    return "sink" in parent


def solve(grid, m, n):
    source = sources(grid, m, n)
    sink = sinks(grid, m, n)
    res = residual(grid, m, n)
    parent = dict()
    max_flow = 0
    while bfs(grid, m, n, source, sink, parent, res):
        min_flow = int(1e9)
        u = parent["sink"]
        while parent[u] != "source":
            min_flow = min(min_flow, res[parent[u]][u])
            u = parent[u]
        u = parent["sink"]
        while parent[u] != "source":
            res[parent[u]][u] -= min_flow
            res[u][parent[u]] += min_flow
            u = parent[u]
        max_flow += min_flow
        parent = dict()
    print(max_flow)


for _ in range(int(input())):
    m, n = map(int, input().split())
    grid = ["." * (n+2)]
    grid += ["." + str(input()) + "." for _ in range(m)]
    grid += ["." * (n+2)]
    solve(grid, m+2, n+2)
