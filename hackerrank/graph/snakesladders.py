from queue import Queue


for _ in range(int(input())):
    ladders = dict()
    for _ in range(int(input())):
        u, v = list(map(int, input().split()))
        ladders[u] = v
    snakes = dict()
    for _ in range(int(input())):
        u, v = list(map(int, input().split()))
        snakes[u] = v
    vis = [False for _ in range(101)]
    q = Queue()
    q.put(1)
    vis[1] = True
    level = 0
    while not q.empty() and not vis[100]:
        size = q.qsize()
        level += 1
        for _ in range(size):
            c = q.get()
            for u in range(c+1, c+7):
                if u > 100 or vis[u]:
                    continue
                elif u in snakes:
                    if not vis[snakes[u]]:
                        vis[snakes[u]] = True
                        q.put(snakes[u])
                elif u in ladders:
                    if not vis[ladders[u]]:
                        vis[ladders[u]] = True
                        q.put(ladders[u])
                elif not vis[u]:
                    vis[u] = True
                    q.put(u)
    if vis[100]:
        print(level)
    else:
        print(-1)
