for _ in range(int(input())):
    n = int(input())
    g = [list(map(int, input().split())) for _ in range(2 * n)]
    r = 0
    for i in range(n):
        for j in range(n):
            r += max(g[i][j], g[2*n-i-1][j], g[i][2*n-j-1], g[2*n-i-1][2*n-j-1])
    print(r)
