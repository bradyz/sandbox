def solve(n, s, memo):
    if n in memo:
        return memo[n]

    result = 0

    for x in s:
        if n != x and n % x == 0:
            result = max(result, 1 + n // x * solve(x, s, memo))

    memo[n] = result

    return result


for _ in range(int(input())):
    n, _ = map(int, input().split())
    s = list(map(int, input().split()))

    print(solve(n, s, dict()))
