for _ in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    min_c = min(c)
    max_c = max(c) - min_c
    ret = 1e9
    for i in [0, 1, 2, 5]:
        t = [c[j] - min_c + i for j in range(n)]
        dp = [1e9 for _ in range(max_c + i + 1)]
        dp[0] = 0
        for i in range(1, max_c + i + 1):
            min_t = 1e9
            if i - 1 >= 0:
                min_t = min(min_t, dp[i-1] + 1)
            if i - 2 >= 0:
                min_t = min(min_t, dp[i-2] + 1)
            if i - 5 >= 0:
                min_t = min(min_t, dp[i-5] + 1)
            dp[i] = min_t
        ret = min(ret, sum(dp[v] for v in t))
    print(ret)
