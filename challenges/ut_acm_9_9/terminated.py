from queue import Queue


def bfs(x, y, ex, ey, g, n):
    q = Queue()
    v = set()

    q.put((x, y, n // 2))
    v.add((x, y))

    while not q.empty():
        x, y, z = q.get()
        if x == ex and y == ey:
            return "ESCAPED"
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                cx, cy, cz = x + dx, y + dy, z + (dy - 1)
                if cx < 0 or cx >= n or cy < 0 or cy >= n:
                    continue
                elif cz <= 0:
                    continue
                elif g[cx][cy] == "#":
                    continue
                elif (cx, cy) in v:
                    continue

                v.add((cx, cy))
                q.put((cx, cy, cz))

    return "TERMINATED"


for _ in range(int(input())):
    n, dy, dx = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    x, y = n // 2, n // 2
    ex, ey = x - dx, y + dy
    print(bfs(x, y, ex, ey, g, n))
