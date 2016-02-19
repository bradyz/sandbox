from queue import Queue


for _ in range(int(input())):
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    adj_list = [list() for _ in range(N)]
    edges_in = [0 for _ in range(N)]
    start = set([u for u in range(N)])
    for i in range(N):
        for j in range(i+1, N):
            if abs(V[i] - V[j]) >= K:
                adj_list[i].append(j)
                edges_in[j] += 1
                if j in start:
                    start.remove(j)
    res = 0
    que = Queue()
    vis = set()
    for u in start:
        res += 1
        que.put(u)
        vis.add(u)
    while not que.empty():
        u = que.get()
        branches = 0
        for v in adj_list[u]:
            if v in vis:
                continue
            edges_in[v] -= 1
            if edges_in[v] == 0:
                branches += 1
                vis.add(v)
                que.put(v)
        if branches > 1:
            res += branches - 1
    print(res)
