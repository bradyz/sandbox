from collections import deque


def bfs():
    v = set()
    ranks = dict()
    q = deque()
    q.append(me)
    l = 0
    while q:
        s = len(q)
        for _ in range(s):
            c = q.popleft()
            if c in v:
                continue
            v.add(c)
            if c != me:
                for x in comp[c]:
                    ranks[x] = ranks.get(x, 0) + 2 ** -l
            for u in graph[c]:
                q.append(u)
        l += 1
    r = []
    for x, y in sorted((-v, k) for k, v in ranks.items()):
        r.append(y)
    print(", ".join(r))


if __name__ == "__main__":
    for t in range(int(input())):
        me = input()
        comp = dict()
        graph = dict()
        graph[me] = list(x.strip() for x in input().split(","))

        for _ in range(int(input())):
            person = input()
            company = tuple(x.strip() for x in input().split(","))
            for f in input().split(","):
                graph[person] = graph.get(person, []) + [f.strip()]
            comp[person] = company

        print(t+1)
        bfs()
