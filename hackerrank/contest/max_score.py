def is_on(x, i):
    return x & (1 << i) > 0


def turn_off(x, i):
    return x & ~(1 << i)


def solve(n, c, run, have, memo=dict()):
    if have not in memo:
        result = 0

        for i in range(n):
            if is_on(have, i):
                score = (run - c[i]) % c[i]
                tmp = turn_off(have, i)

                result = max(result, score + solve(n, c, run - c[i], tmp))

        memo[have] = result

    return memo[have]


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().split()))

    print(solve(n, c, sum(c), int("1" * n, 2)))
