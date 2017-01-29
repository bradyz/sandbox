from itertools import permutations


def win(x, y):
    n = len(x)
    i, j = 0, 0
    while i < n and j < n:
        h1, a1, d1 = x[i]
        h2, a2, d2 = y[j]
        while h1 > 0 and h2 > 0:
            dmg1 = a1 * (1 - d2)
            dmg2 = a2 * (1 - d1)
            h1 -= dmg2
            h2 -= dmg1
        if h1 <= 0:
            i += 1
        if h2 <= 0:
            j += 1
    return n - i


def solve(x, y):
    result = 0
    for order in permutations(x):
        result = max(result, win(order, y))
    return result


n = int(input())
x = [tuple(map(float, input().split()[1:])) for _ in range(n)]
y = [tuple(map(float, input().split()[1:])) for _ in range(n)]
print(solve(x, y))
