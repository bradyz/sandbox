from queue import PriorityQueue


def dijkstra():
    dist = {u: -1 for u in range(1, n+1)}
    dist[s] = 0

    parent = dict()
    parent[s] = -1

    q = PriorityQueue()
    q.put((0, s))

    while not q.empty():
        w, u = q.get()

        for i in range(len(g[u])):
            v = g[u][i]
            w_v = w + weight[u][i]
            if dist[v] == -1 or w_v < dist[v]:
                parent[v] = u
                dist[v] = w_v
                q.put((w_v, v))

    return dist

if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        g = {i: list() for i in range(1, n+1)}
        weight = {i: list() for i in range(1, n+1)}
        for _ in range(m):
            u, v, w = map(int, input().split())
            g[u].append(v)
            g[v].append(u)
            weight[u].append(w)
            weight[v].append(w)
        s = int(input())
        d = dijkstra()
        r = list()
        for x in d:
            if x != s:
                r.append(d[x])
        print(" ".join(map(str, r)))
