def solve(a, b, c, n):
    ai = 0
    bi = 0
    ci = 0
    r = 0
    print(a, b, c)

    while ai < n or bi < n or ci < n:
        if ai < n and bi < n and ci < n:
            if a[ai] <= b[bi] and a[ai] <= c[ci]:
                r += 2
                ai += 1
            elif b[bi] <= a[ai] and b[bi] <= c[ci]:
                r += 2
                bi += 1
            else:
                r += 2
                ci += 1
        elif ai < n and bi < n:
            if a[ai] <= b[bi]:
                r += 1
                ai += 1
            else:
                r += 1
                bi += 1
        elif bi < n and ci < n:
            if b[bi] <= c[ci]:
                r += 1
                bi += 1
            else:
                r += 1
                ci += 1
        elif ai < n and ci < n:
            if a[ai] <= c[ci]:
                r += 1
                ai += 1
            else:
                r += 1
                ci += 1
        elif ai < n:
            ai += 1
        elif bi < n:
            bi += 1
        elif ci < n:
            ci += 1
        # print(ai, bi, ci)

    return r

if __name__ == "__main__":
    for i in range(1, 8):
        t = list(range(i))
        print(solve(t, t, t, len(t)))
