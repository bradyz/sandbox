def lines(v):
    r = 0
    x = 0
    while v // (k ** x) != 0:
        r += v // (k ** x)
        x += 1
    return r


def solve():
    low = 0
    high = 1000000000-1

    while low+1 < high:
        mid = (low + high) // 2

        if lines(mid) >= n:
            high = mid
        else:
            low = mid

    print(high)


n, k = map(int, input().split())
solve()
