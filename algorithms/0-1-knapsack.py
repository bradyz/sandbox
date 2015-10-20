import pprint


def knapsack(w, v, c):
    pp = pprint.PrettyPrinter(indent=0)
    dp = [[0 for _ in range(c+1)] for _ in range(len(v)+1)]
    for i in range(len(v) + 1):
        for j in range(c+1):
            if i > 0 and j > 0:
                if w[i-1] <= j:
                    dp[i][j] = dp[i-1][j-w[i-1]] + v[i-1]
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1], dp[i][j])

    pp.pprint(dp)

if __name__ == "__main__":
    _w = [1, 5, 3, 4]
    _v = [15, 10, 9, 5]
    _c = 8
    knapsack(_w, _v, _c)
