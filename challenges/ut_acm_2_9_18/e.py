from collections import defaultdict, deque


def bfs(start):
    q = deque()
    vis = set([start])

    q.appendleft((start, 0))

    while q:
        u, d = q.pop()

        for v in graph[u]:
            if v == start:
                return d + 1
            elif v in vis:
                continue

            vis.add(v)
            q.appendleft((v, d + 1))

    return int(1e9)



n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())

    graph[u].append(v)

result = min(bfs(u) for u in list(graph.keys()))

if result == int(1e9):
    print(-1)
else:
    print(result)
