from bisect import bisect_right


def memo(n):
    if n < 0:
        return 0
    elif dp[n] >= 0:
        return dp[n]
    dp[n] = memo(n-1) + memo(n-4)
    return dp[n]


def sieve():
    prime[0] = False
    prime[1] = False
    for i in range(2, 1000000):
        if not prime[i]:
            continue
        prime_list.append(i)
        for j in range(i+i, 1000000, i):
            prime[j] = False

if __name__ == "__main__":
    prime = [True for _ in range(1000000)]
    prime_list = list()
    sieve()
    dp = [-1 for _ in range(41)]
    dp[0] = 1
    for _ in range(int(input())):
        N = int(input())
        print(bisect_right(prime_list, memo(N)))
    print(dp)
