def solve(n, k, c):
    need = 0
    need_to_cover = c[0]

    i = 1
    while i < n:
        if c[i] - k > need_to_cover:
            need += 1
            need_to_cover = c[i-1] + k + 1
            while i < n and need_to_cover > c[i]:
                i += 1
            if i < n:
                need_to_cover = c[i]
        i += 1

    if c[-1] >= need_to_cover:
        need += 1

    return need


if __name__ == '__main__':
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    c.sort()

    print(solve(n, k, c))
