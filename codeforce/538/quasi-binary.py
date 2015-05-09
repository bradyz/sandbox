def b(n):
    return int(bin(n).lstrip("0b"))


def p(c):
    for d in c:
        print(d[2:])


def solve(n):
    c = int(len(str(n)) * "1", 2)
    dp = [[-1 for j in range(c+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(c+1):
            if i == 0 or j == 0:
                dp[i][j] = []
            elif j == 1:
                dp[i][j] = dp[i-1][j] + [1]
            else:
                if i-b(j) >= 0:
                    if len(dp[i-b(j)][j]) + 1 < len(dp[i][j-1]):
                        dp[i][j] = dp[i-b(j)][j] + [b(j)]
                    else:
                        dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

    print(len(dp[n][c]))
    print(" ".join(map(str, dp[n][c])))

if __name__ == "__main__":
    num = int(input())
    solve(num)
