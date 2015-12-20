if __name__ == "__main__":
    for _ in range(int(input())):
        N = int(input())
        val = [0] + [int(x) for x in input().split()]
        pre = val[::]
        for i in range(1, N+1):
            pre[i] += pre[i-1]
        dp = [-1 for _ in range(N+1)]
        for i in range(N+1):
            if i == 0:
                dp[i] = 0
            elif i == 1:
                dp[i] = val[i]
            elif i == 2 or i == 3:
                dp[i] = dp[i-1] + val[i]
            else:
                dp[i] = max(dp[i], pre[i-1]-dp[i-1]+val[i])
                dp[i] = max(dp[i], pre[i-2]-dp[i-2]+val[i]+val[i-1])
                dp[i] = max(dp[i], pre[i-3]-dp[i-3]+val[i]+val[i-1]+val[i-2])
        print(pre)
        print(dp)
        print(dp[N])
