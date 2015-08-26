def median(c):
    if len(c) % 2 == 0:
        return (c[len(c) // 2] + c[len(c) // 2 - 1]) // 2
    else:
        return c[len(c) // 2]


def solve(c, d, n):
    # print(c, d, n)

    if n == 1:
        return c[0]
    elif n == 2:
        return (max(c[0], d[0]) + min(c[1], d[1])) // 2

    m1 = median(c)
    m2 = median(d)

    if m1 == m2:
        return m1
    else:
        if m1 > m2:
            c, d = d, c
        if n % 2 == 0:
            return solve(c[n // 2 - 1:], d[:n // 2], n - n // 2 - 1)
        else:
            return solve(c[n // 2:], d[:n // 2 + 1], n - n // 2)


# arrays must be of the same size
if __name__ == "__main__":
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    print(solve(arr_1, arr_2, len(arr_1)))
