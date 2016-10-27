def binary_search(x, c, lo, hi):
    while lo < hi:
        mi = (lo + hi) // 2
        if c[mi] < x:
            lo = mi + 1
        else:
            hi = mi
    return lo


def lis(n, c):
    best = [None for _ in range(n+1)]
    best[0] = -1
    best[1] = c[0]
    result = 1
    for i in range(1, n):
        j = binary_search(c[i], best, 1, result+1)
        if not best[j]:
            best[j] = c[i]
            result += 1
        elif c[i] < best[j]:
            best[j] = c[i]
    return best[1:result+1]


if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().split()))
    r = lis(n, c)
    print(r)
