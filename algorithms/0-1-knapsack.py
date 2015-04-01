def knapsack(w, b, c):
    dp = [[0 for _ in range(c+1)] for _ in range(len(b)+1)]
    for i in range(len(b) + 1):
        for j in range(len(w) + 1):
            if i > 0 and j > 0:
                x = dp[i-1][j] + b[i-1]
                y = dp[i][j-1] + b[i-1]
                if j + w[i-1] < c:
                    dp[i][j] = max(x, y, dp[i-1][j-1])
                else:
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

    print(dp)

if __name__ == "__main__":
    _w = [2, 3, 4, 5]
    _b = [3, 4, 5, 6]
    _c = 5
    knapsack(_w, _b, _c)
