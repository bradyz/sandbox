from queue import Queue


def solve(home, city1, city2, graph, country, restrictions):
    que = Queue()
    visited = set([city1])
    que.put((city1, -1))

    while not que.empty():
        u, steps = que.get()
        if u == city2:
            return max(0, steps)
        for v in graph.get(u, list()):
            if v in visited:
                continue
            elif country[v] == country[u]:
                que.put((v, steps + 1))
                visited.add(v)
            elif home not in restrictions.get(country[v], set()):
                que.put((v, steps + 1))
                visited.add(v)

    return "IMPOSSIBLE"


for _ in range(int(input())):
    flights, restriction, queries = map(int, input().split())

    graph = dict()
    country = dict()
    restrictions = dict()

    for _ in range(flights):
        city1, country1, _, city2, country2 = input().split()
        country[city1] = country1
        country[city2] = country2
        if city1 not in graph:
            graph[city1] = list()
        graph[city1].append(city2)

    for _ in range(restriction):
        country1, _, country2 = input().split()
        if country2 not in restrictions:
            restrictions[country2] = set()
        restrictions[country2].add(country1)

    for _ in range(queries):
        home, city1, country1, _, city2, country2 = input().split()
        print(solve(home, city1, city2, graph, country, restrictions))
