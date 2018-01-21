from collections import deque


def bfs(g, r, c, si, sj, ti, tj):
    q = deque()
    q.append((si, sj, 1))
    v = set([(si, sj)])

    while len(q) > 0:
        i, j, s = q.pop()

        if i == ti and j == tj:
            return s

        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            ni, nj = i + di, j + dj

            if ni < 0 or ni >= r:
                continue
            elif nj < 0 or nj >= c:
                continue
            elif g[ni][nj] != g[si][sj]:
                continue
            elif (ni, nj) in v:
                continue

            v.add((ni, nj))
            q.append((ni, nj, s + 1))

    return -1


r, c = map(int, input().split())
g = [input() for _ in range(r)]
si, sj = map(int, input().split())
ti, tj = map(int, input().split())

print(bfs(g, r, c, si, sj, ti, tj))
