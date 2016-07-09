INF = int(1e9)


class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
        # 0: noop, 1: buy, 2: sell
        dp = [[[-INF for _ in range(3)] for _ in range(2)] for _ in range(n)]
        dp[0][0][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, n):       # day
            dp[i][0][0] = max(dp[i-1][0])
            dp[i][0][2] = max(dp[i-1][1]) + prices[i]
            dp[i][1][0] = max(dp[i-1][1])
            dp[i][1][1] = max(dp[i-1][0][0], dp[i-1][0][1]) - prices[i]
        return max(dp[n-1][i][j] for i in range(2) for j in range(3))


s = Solution()
prices = [2, 1, 4, 5, 2, 9, 7]
a = s.maxProfit(prices)
print(a)
