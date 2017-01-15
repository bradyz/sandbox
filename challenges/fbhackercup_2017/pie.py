INF = float("inf")


def solve(n, m, c):
    extra = {0: 0}

    for i in range(n):
        new_extra = {0: 0}

        total = 0
        for j in range(m):
            total += c[i][j]
            cost = total + (j + 1) ** 2
            new_extra[j + 1] = cost

        combined = dict()

        for k1, v1 in extra.items():
            for k2, v2 in new_extra.items():
                if k1 + k2 - 1 < 0 or k1 + k2 > n - i:
                    continue
                combined[k1 + k2 - 1] = min(combined.get(k1 + k2 - 1, INF),
                                            v1 + v2)

        extra = combined

    return min(extra.values())


for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    c = [list(sorted(map(int, input().split()))) for _ in range(n)]
    print("Case #%d: %d" % (i, solve(n, m, c)))
