# 363B: Fency
# Start Time: 10:35 p.m. 4-30-15
# End Time: 10:51 p.m. 4-30-15

from copy import copy


def solve(n, l, c):
    s = copy(c)

    # array of sums of values
    for i in range(1, n):
        s[i] += s[i-1]

    dp = [0 for _ in range(n-l+1)]

    # moving window of size l
    for i in range(n-l+1):
        if i == 0:
            dp[i] = s[l-1]
        else:
            dp[i] = s[i+l-1] - s[i-1]

    # O(2n) but accepted so its fine
    return dp.index(min(dp)) + 1

if __name__ == "__main__":
    args = list(map(int, input().split()))
    num_planks = args[0]
    window_length = args[1]
    planks = list(map(int, input().split()))

    print(solve(num_planks, window_length, planks))
