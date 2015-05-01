# 466C: Number Ways
# Start Time: 10:11 a.m. 5-1-15
# End Time: 10:50 a.m. 4-28-15


# brute force O(n^3) tle on test 6 @ 10:18 a.m.
def solve(n, c):
    count = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            if sum(c[:i]) == sum(c[i:j]) == sum(c[j:]):
                count += 1
    return count


def solve1(n, c):
    dp = [0 for _ in range(n)]
    poss = []
    count = 0

    for i in range(n):
        dp[i] = c[i] + dp[i-1] if i > 0 else c[i]

    if (dp[n-1] / 3) % 1 != 0:
        return 0

    for i in range(n-2):
        if dp[i] == dp[n-1] // 3:
            poss.append(i+1)

    for i in poss:
        for j in range(i, n-1):
            if dp[j] - dp[i-1] == dp[n-1] // 3:
                count += 1

    return count

if __name__ == "__main__":
    num_el = int(input())
    values = list(map(int, input().split()))
    print(solve1(num_el, values))
