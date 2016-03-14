def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n):
        dp[1][i] = a[i]

    for i in range(2, n+1):
        for j in range(i-1, n):
            dp[i][j] = gcd(a[j], dp[i-1][j-1])

    print("\n".join(map(str, dp)))
