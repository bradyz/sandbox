from sys import maxsize as INT_MAX


def floydwarshall():
    for i in range(1, n+1):
        g[i][i] = 0
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if g[i][k] == -1 or g[k][j] == -1:
                    continue
                elif g[i][j] == -1:
                    g[i][j] = g[i][k] + g[k][j]
                else:
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])

if __name__ == "__main__":
    n = int(input())
    g = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    best = INT_MAX
    for _ in range(n-1):
        u, v = map(int, input().split())
        g[u][v] = 1
        g[v][u] = 1
    floydwarshall()
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            pair_score = -1
            for k in range(1, n+1):
                dist = min(g[i][k], g[j][k])
                pair_score = max(pair_score, dist)
            best = min(best, pair_score)
    print(best)
