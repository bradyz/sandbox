from queue import Queue


def search(u, g, vis, done, cycle):
    vis.add(u)
    for v in g.get(u, []):
        if v not in vis and search(v, g, vis, done, cycle):
            done.add(u)
            cycle.add(v)
            return True
        elif v not in done:
            done.add(u)
            cycle.add(v)
            return True
    done.add(u)
    return False


def has_cycle(g):
    vis = set()
    done = set()
    cycles = list()
    for u in g:
        if u in vis:
            continue
        cycles.append(set())
        search(u, g, vis, done, cycles[-1])
    return cycles


def bfs(x):
    q = Queue()
    vis = set()
    q.put(x)
    vis.add(x)
    while not q.empty():
        u = q.get()
        for v in g[u]:
            if v in vis:
                continue
            vis.add(v)
            q.put(v)
    return vis


n, m = map(int, input().split())
g = {u: list() for u in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

cycles = [x for x in has_cycle(g) if x]
cycles_can_reach = [bfs(cycle.pop()) for cycle in cycles]
in_cycle = set()
for cycle in cycles:
    for u in cycle:
        in_cycle.add(u)
one_vis = bfs(1)

incoming = {u: 0 for u in range(1, n+1)}
for u in g:
    if u in in_cycle:
        continue
    for v in g[u]:
        if v in in_cycle:
            continue
        incoming[v] += 1

dp = [0 for _ in range(n+1)]
dp[1] = 1
que = Queue()
for u in incoming:
    if incoming[u] == 0:
        que.put(u)
while not que.empty():
    u = que.get_nowait()
    if u in in_cycle:
        continue
    for v in g[u]:
        if v in in_cycle:
            continue
        incoming[v] -= 1
        dp[v] = (dp[v] + dp[u]) % int(1e9)
        if incoming[v] == 0:
            que.put(v)

can = True
for cycle, can_reach in zip(cycles, cycles_can_reach):
    node_with_cycle = cycle.pop()
    if node_with_cycle in one_vis and n in can_reach:
        can = False
if can:
    print(dp[n])
else:
    print("INFINITE PATHS")
