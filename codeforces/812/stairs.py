INF = float('inf')


def solve(grid, n, m):
    dp = [[INF for _ in range(2)] for _ in range(n)]

    dp[0][0] = -1
    dp[0][1] = INF

    for i in range(1, n):
        occur = [j for j in range(m+2) if grid[i-1][j] == '1']

        if not occur:
            dp[i][0] = min(dp[i][0], dp[i-1][0] + 1)
            dp[i][0] = min(dp[i][0], dp[i-1][1] + (m + 2))

            dp[i][1] = min(dp[i][1], dp[i-1][0] + (m + 2))
            dp[i][1] = min(dp[i][1], dp[i-1][1] + 1)
            continue

        dp[i][0] = min(dp[i][0], dp[i-1][0] + (2 * max(occur)) + 1)
        dp[i][0] = min(dp[i][0], dp[i-1][1] + (m + 2))

        dp[i][1] = min(dp[i][1], dp[i-1][0] + (m + 2))
        dp[i][1] = min(dp[i][1], dp[i-1][1] + (2 * (m + 2 - min(occur) - 1) + 1))

    occur = [j for j in range(m+2) if grid[n-1][j] == '1']

    return min(dp[n-1][0] + max(occur) + 1, dp[n-1][1] + (m + 2 - min(occur)))


if __name__ == '__main__':
    n, m = map(int, input().split())

    grid = [input() for _ in range(n)]
    grid.reverse()

    n_real = -1
    for i in range(n-1, -1, -1):
        if '1' in grid[i]:
            n_real = i
            break

    if n_real == -1:
        print(0)
    else:
        print(solve(grid[:n_real+1], n_real+1, m))
