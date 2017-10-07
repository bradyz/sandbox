n = int(input())
beauties = list(map(int, input().split()))

graph = {u: list() for u in range(1, n+1)}

for _ in range(n-1):
    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)

edges = list()

stack = [1]
visited = set([1])

while stack:
    u = stack.pop()

    for v in graph[u]:
        if v in visited:
            continue

        visited.add(v)
        edges.append((u, v))

        stack.append(v)

outgoing = {i: set() for i in range(1, n+1)}
incoming = {i: set() for i in range(1, n+1)}

for u, v in edges:
    outgoing[v].add(u)
    incoming[u].add(v)

lone = list()

for i in range(1, n+1):
    if not incoming[i]:
        lone.append(i)

memo = {i: beauties[i-1] for i in range(1, n+1)}

while lone:
    u = lone.pop()

    for v in outgoing[u]:
        memo[v] += max(0, memo[u])
        incoming[v].remove(u)

        if not incoming[v]:
            lone.append(v)

print(max(memo.values()))
