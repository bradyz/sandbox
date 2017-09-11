def primes(n):
    result = set()

    while n % 2 == 0:
        result.add(2)
        n //= 2

    x = 3

    while x * x <= n:
        while n % x == 0:
            result.add(x)
            n //= x

        x += 2

    if n != 1:
        result.add(n)

    return result


petals_flowers = [list(map(int, input().split())) for _ in range(int(input()))]

points = dict()

for petals, flowers in petals_flowers:
    for factor in primes(petals):
        points[factor] = points.get(factor, 0) + petals

print(max(points.values()))
