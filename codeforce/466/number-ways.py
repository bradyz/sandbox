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


# O(n^2) solution
def solve1(n, c):
    dp = [0 for _ in range(n)]
    count = 0

    for i in range(n):
        dp[i] = c[i] + dp[i-1] if i > 0 else c[i]

    third = dp[n-1] // 3

    if third * 3 != dp[n-1]:
        return 0

    for i in range(n-2):
        if dp[i] == third:
            for j in range(i+1, n-1):
                if dp[j] - dp[i] == third:
                    count += 1

    return count


def solve2(n, c):
    dp = [0 for _ in range(n)]
    r = 0
    p = 0

    for i in range(n):
        dp[i] = c[i] + dp[i-1] if i > 0 else c[i]

    t = dp[n-1] // 3

    if t * 3 != dp[n-1]:
        return 0

    for i in range(n-1):
        if dp[i] == 2 * t:
            r += p
        if dp[i] == t:
            p += 1

    return r

if __name__ == "__main__":
    num_el = int(input())
    values = list(map(int, input().split()))
    print(solve2(num_el, values))
