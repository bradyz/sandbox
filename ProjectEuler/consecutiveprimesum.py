def primes_below(n):
    p = [True for _ in range(n)]
    r = [0]
    for i in range(2, n):
        if p[i]:
            for j in range(i + i, n, i):
                p[j] = False
            r.append(i)
    return r


# i misread the question
def solve(n, p):
    dp = [[-1 for j in range(len(p)+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(len(p)+1):
            if i == j or j == 0:
                dp[i][j] = 0
            else:
                if i - p[j-1] >= 0:
                    dp[i][j] = dp[i-p[j-1]][j] + 1
                dp[i][j] = max(dp[i][j], dp[i][j-1])
    from pprint import PrettyPrinter
    pp = PrettyPrinter()
    pp.pprint(dp)
    return 0


def solve1(n):
    p = primes_below(n)
    s = set(p)
    r = 0
    a = 0

    for i in range(1, len(p)):
        p[i] += p[i-1]

    for i in range(len(p)):
        for j in range(i+a, len(p)):
            if p[j]-p[i] in s:
                r = p[j]-p[i]
                a = j-i
    print(r)

if __name__ == "__main__":
    solve1(1000000)
