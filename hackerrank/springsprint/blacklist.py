import sys


def min_cost(n, k, c):
    dp = [[-1 for _ in range(n+1)] for _ in range(k+1)]
    c = sorted(c, key=lambda x: x[0])
    for a in c:
        print(a)
    print("\n")
    for i in range(k+1):
        for j in range(n+1):
            if i == 0:
                dp[i][j] = 10000
            elif j == 0:
                dp[i][j] = 0
            else:
                dp[i][j] = min(c[i-1][j-1]+dp[i][j-1], dp[i-1][j])
                for d in dp:
                    print(d)
                print("\n")
    print(dp[k][n])

if __name__ == "__main__":
    _c = []
    for i, line in enumerate(sys.stdin):
        if i == 0:
            args = map(int, line.split())
            _n = args[0]
            _k = args[1]
        else:
            _c.append(map(int, line.split()))
    min_cost(_n, _k, _c)
