def solve(c, d, n, m):
    i, j = 0, 0
    r = None

    while i + j < (n + m) // 2:
        if i < n and c[i] < d[j]:
            r = c[i]
            i += 1
        else:
            r = d[j]
            j += 1

    print(r)

if __name__ == "__main__":
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))

    solve(arr_1, arr_2, len(arr_1), len(arr_2))
