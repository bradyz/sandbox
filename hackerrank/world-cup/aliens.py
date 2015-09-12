from sys import maxsize as MAXINT
from queue import Queue

def bfs(x, y, d1, d2, d3, d4):
    q = Queue()
    q.put((x, y))
    l = 0
    z = []

    while not q.empty():
        t = q.qsize()

        while t > 0:
            x, y = q.get()

            if x < 0 or y < 0 or x >= n or y >= m or g[x][y] == ".":
                break
            elif v[x][y]:
                l = 0
                break

            z.append((x, y))
            q.put((x+d1, y+d2))

            if t == 1:
                q.put((x+d3, y+d4))

            t -= 1

        if t > 0:
            break

        l += 1

    if l > 1:
        for x, y in z:
            v[x][y] = True
        return l

    return 0


def solve():
    def neighbors(x, y):
        a, d = 0, 0
        for i in (-1, 0, 1):
            for j in (-1, 0, 1):
                if i == 0 and j == 0:
                    continue
                elif x+i < 0 or x+i >= n or y+j < 0 or y+j >= m or \
                        g[x+i][y+j] == ".":
                    continue

                if i == 0 or j == 0:
                    a += 1
                else:
                    d += 1

        return a == 1 and d == 1

    t = MAXINT
    f = False

    for i in range(n):
        for j in range(m):
            if g[i][j] == "#":
                f = True
            if g[i][j] == "." or not neighbors(i, j):
                continue

            w[i][j] = max(w[i][j], bfs(i, j, 1, 0, 1, 1))
            w[i][j] = max(w[i][j], bfs(i, j, 1, 0, 1, -1))

            if i == 3 and j == 0:
                print(bfs(i, j, -1, 0, -1, 1))
            w[i][j] = max(w[i][j], bfs(i, j, -1, 0, -1, 1))
            w[i][j] = max(w[i][j], bfs(i, j, -1, 0, -1, -1))

            w[i][j] = max(w[i][j], bfs(i, j, 0, 1, 1, 1))
            w[i][j] = max(w[i][j], bfs(i, j, 0, 1, -1, 1))

            w[i][j] = max(w[i][j], bfs(i, j, 0, -1, -1, -1))
            w[i][j] = max(w[i][j], bfs(i, j, 0, -1, 1, -1))

            print(i, j, w[i][j])

    print("\n".join(map(str, w)))

    for i in range(n):
        for j in range(m):
            if w[i][j] > 0:
                t = min(t, w[i][j])

    if t == MAXINT:
        if f:
            return 1
        else:
            return 0
    else:
        return t

if __name__ == "__main__":
    n, m = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    w = [[0 for _ in range(m)] for _ in range(n)]
    v = [[False for _ in range(m)] for _ in range(n)]

    print(solve())
