from sys import maxsize as INT_MAX
import heapq


def dijkstra(graph, src, n):
    dist = [-1 for _ in range(n)]
    dist[src] = 0

    q = []
    heapq.heappush(q, (0, src))

    while q:
        w, u = heapq.heappop(q)

        for v in range(n):
            if graph[u][v] == 0:
                continue

            nw = w + graph[u][v]

            if dist[v] == -1 or nw < dist[v]:
                dist[v] = nw
                heapq.heappush(q, (nw, v))

    # print distances from source
    for i in range(n):
        print(i, dist[i])

    return dist



# O(V^2) time complexity
def dijkstraV2(graph, src, n):

    # returns the minimum closest vertex not yet visited
    def min_dist():
        min_v = INT_MAX
        min_i = -1

        # looks for minimum index in updated distance array
        for i in range(n):
            if not spt[i] and dist[i] < min_v:
                min_v = dist[i]
                min_i = i

        return min_i

    spt = [False for _ in range(n)]     # included in solution
    dist = [INT_MAX for _ in range(n)]  # distances from source
    dist[src] = 0                       # starts from the source

    # O(V) for each vertex
    for i in range(n):
        u = min_dist()                  # will start from source
        spt[u] = True                   # mark solution found

        # O(V) that can be easily improved with heap data structure
        for v in range(n):
            if not spt[v] and graph[u][v] and dist[u]+graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    # print distances from source
    for i in range(n):
        print(i, dist[i])

if __name__ == "__main__":
    adj_graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                 [4, 0, 8, 0, 0, 0, 0, 11, 0],
                 [0, 8, 0, 7, 0, 4, 0, 0, 2],
                 [0, 0, 7, 0, 9, 14, 0, 0, 0],
                 [0, 0, 0, 9, 0, 10, 0, 0, 0],
                 [0, 0, 4, 0, 10, 0, 2, 0, 0],
                 [0, 0, 0, 14, 0, 2, 0, 1, 6],
                 [8, 11, 0, 0, 0, 0, 1, 0, 7],
                 [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    dijkstra(adj_graph, 0, len(adj_graph))
    print()
    dijkstraV2(adj_graph, 0, len(adj_graph))
