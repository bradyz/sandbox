from collections import deque, defaultdict


incoming = defaultdict(set)
outgoing = defaultdict(set)

for _ in range(int(input())):
    u, v = input().split()

    outgoing[u].add(v)
    incoming[v].add(u)

queue = deque()
queue.append('JFK')

ways = defaultdict(int)
ways['JFK'] = 1

while queue:
    u = queue.popleft()

    for v in outgoing[u]:
        incoming[v].remove(u)
        ways[v] += ways[u]

        if not incoming[v]:
            queue.append(v)

print(ways['SFO'])
