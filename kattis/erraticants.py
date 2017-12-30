from collections import deque


DIR = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}


def bfs(s, t, graph):
    q = deque()
    q.appendleft(s)

    dist = {s: 0}

    while len(q) > 0:
        u = q.popleft()

        if u == t:
            break

        for v in graph.get(u, set()):
            if v in dist:
                continue

            dist[v] = dist[u] + 1
            q.append(v)

    return dist[t]


def solve(c):
    x = 0
    y = 0

    graph = dict()
    graph[(0, 0)] = set()

    for dx, dy in map(lambda key: DIR[key], c):
        nx, ny = x + dx, y + dy

        if (nx, ny) not in graph:
            graph[(nx, ny)] = set()

        graph[(nx, ny)].add((x, y))
        graph[(x, y)].add((nx, ny))

        x = nx
        y = ny

    print(bfs((0, 0), (x, y), graph))


for _ in range(int(input())):
    input()

    solve([input() for _ in range(int(input()))])
