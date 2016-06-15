from Queue import Queue


def answer(g, x, y, s):
    n = 25
    m = 25

    q = Queue()
    v = set()

    if g[y][x] <= s:
        g[y][x] = -1
        q.put((x, y))
        v.add((x, y))

    while not q.empty():
        cx, cy = q.get()

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= m or ny < 0 or ny >= n or (nx, ny) in v:
                continue
            v.add((nx, ny))
            try:
                if g[ny][nx] <= s:
                    g[ny][nx] = -1
                    q.put((nx, ny))
            except:
                pass

    return g


population = [[9, 3, 4, 5, 4],
              [1, 6, 5],
              [3, 4, 5, 8, 1],
              [4, 5, 4, 3, 9]]
x = 2
y = 1
strength = 5
print(answer(population, x, y, strength))
