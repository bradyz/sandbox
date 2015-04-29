# 489B: BerSU Ball
# Start: 1:03 a.m. 4-29-15
# End: 1:18 a.m. 4-29-15

# from pprint import PrettyPrinter


def solve(m, n, c, d):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    # pp = PrettyPrinter(indent=1)

    for i in range(n+1):
        for j in range(m+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            else:
                if abs(d[i-1] - c[j-1]) <= 1:
                    dp[i][j] = dp[i-1][j-1] + 1
                dp[i][j] = max(dp[i][j], dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
                # pp.pprint(dp)
                # print()

    return dp[n][m]


if __name__ == "__main__":
    b = int(input())
    bc = list(map(int, input().split()))

    g = int(input())
    gc = list(map(int, input().split()))

    print(solve(b, g, sorted(bc), sorted(gc)))
