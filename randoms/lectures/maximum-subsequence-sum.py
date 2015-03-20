import sys


def max_subseq(a):
    dp = [-sys.maxsize for _ in range(len(a)+1)]

    for i in range(len(a)):
        dp[i+1] = max(dp[i]+a[i], a[i])
        print(dp)

    return max(dp)

if __name__ == "__main__":
    _a = [-2, 11, -4, 13, -5, 4, -2]
    print(max_subseq(_a))
