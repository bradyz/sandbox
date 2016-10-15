from math import sqrt
from itertools import permutations


def pretty(t):
    hours = int(t)
    t -= hours
    t *= 60
    minutes = int(t)
    t -= minutes
    t *= 60
    seconds = round(t)
    return "%d hour(s) %d minutes(s) %d second(s)" % (hours, minutes, seconds)


def amount(x, y, v, vx, vy, vvx, vvy):
    a, b, c = 0, 0, 0

    # a * x ^ 2 + b * x + c = 0
    a += vvx * vvx
    a += vvy * vvy
    a -= v * v

    b += 2 * vvx * (vx - x)
    b += 2 * vvy * (vy - y)

    c += (vx - x) ** 2
    c += (vy - y) ** 2

    if b * b - 4 * a * c < 0:
        raise Exception("imaginary")

    nt1 = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    nt2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)

    if nt1 < 0:
        return nt2
    elif nt2 < 0:
        return nt1

    return min(nt1, nt2)


def solve(x, y, v, vessels, t=0):
    vx, vy, vvx, vvy = vessels[0]
    vx, vy = vx + t * vvx, vy + t * vvy

    # time to get there
    dt = amount(x, y, v, vx, vy, vvx, vvy) + 1

    mx = vx + dt * vvx
    my = vy + dt * vvy

    if len(vessels) == 1:
        return t + dt + sqrt(mx * mx + my * my) / v

    return solve(mx, my, v, vessels[1:], t + dt)


if __name__ == "__main__":
    for test in range(1, int(1e9)):
        n = int(input())
        if n == 0:
            break

        vessels = [list(map(int, input().split())) for _ in range(n)]
        x, y, v = map(int, input().split())
        time = int(1e9)

        for order in permutations(list(range(n))):
            tmp = solve(x, y, v, list(map(lambda x: vessels[x], order)))
            time = min(time, tmp)

        print("Case %d: %s" % (test, pretty(time)))
