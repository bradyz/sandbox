import heapq


def dijkstra(graph, src):
    cost = {src: 0}
    q = [(0, src)]
    while q:
        w, u = heapq.heappop(q)
        for vv, vw in graph[u]:
            nw = w + vw
            if nw < cost.get(vv, int(1e9)):
                cost[vv] = nw
                heapq.heappush(q, (nw, vv))
    return cost


def solve(start, start_ammo, dests, outposts, ammo, ammo_bonus):
    best = int(1e9)

    dist = dijkstra(outposts, start)
    for target in dests:
        if target in dist and dist[target] <= start_ammo:
            best = min(best, dist[target])

    if not ammo_bonus:
        return best

    dist = dijkstra(outposts, ammo)

    if start not in dist or start_ammo < dist[start]:
        return best

    new_ammo = start_ammo - dist[start] + ammo_bonus
    for target in dests:
        if target not in dist:
            continue
        elif dist[target] > new_ammo:
            continue
        best = min(best, dist[start] + dist[target])

    return best


for _ in range(int(input())):
    n, m = map(int, input().split())

    ammo = None
    ammo_amount = None
    source = None
    source_amount = None

    dests = set()
    outposts = dict()

    for i in range(n):
        x, y, z = input().split()
        outposts[x] = list()
        if i == 0:
            source = x
            source_amount = int(y)

        if z == "yes":
            dests.add(x)
        elif i > 0 and int(y) > 0:
            ammo = x
            ammo_amount = int(y)

    for _ in range(m):
        x, y, z = input().split()
        outposts[x].append((y, int(z)))
        outposts[y].append((x, int(z)))

    best = solve(source, source_amount, dests, outposts, ammo, ammo_amount)

    if best == int(1e9):
        print("No safe path")
    else:
        print(best)
