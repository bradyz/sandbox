def solve(c, n, s):
    dp = [[False for _ in range(n+1)] for _ in range(s+1)]
    for i in range(n+1):
        dp[0][i] = True
    for i in range(1, s+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]
            if i < c[j-1]:
                continue
            dp[i][j] |= dp[i - c[j-1]][j-1]

    r = int(1e9)
    half = s / 2
    for i in range(s+1):
        for j in range(n+1):
            if dp[i][j] and abs(i - half) < abs(r - half):
                r = i
    # print("\n".join(map(str, dp)))
    print(abs(r - (s - r)))


for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    s = sum(c)
    solve(c, n, s)
