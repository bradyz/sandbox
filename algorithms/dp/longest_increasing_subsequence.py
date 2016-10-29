def binary_search(x, c):
    lo = 1
    hi = len(c)
    while lo < hi:
        mi = (lo + hi) // 2
        if c[mi] < x:
            lo = mi + 1
        else:
            hi = mi
    return lo


def lis(n, c):
    best = [float("-inf"), c[0]]
    for i in range(1, n):
        j = binary_search(c[i], best)
        if j == len(best):
            best.append(c[i])
        elif c[i] < best[j]:
            best[j] = c[i]
    return best[1:]


if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().split()))
    r = lis(n, c)
    print(r)
