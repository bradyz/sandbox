for _ in range(int(input())):
    a, b, d = map(int, input().split())
    a, b = min(a, b), max(a, b)

    result = float("inf")

    # case 1, use 0 a's
    tmp = max(d // b - 1, 0)
    if d % b != 0:
        tmp += 2
    result = min(result, tmp)
    # case 2, use 1 a's
    if d - a >= 0:
        tmp = 1 + (d - a) // b
        if (d - a) % b != 0:
            tmp += 2
        result = min(result, tmp)
    # case 3, use 2 a's
    if d - 2 * a >= 0:
        tmp = 2 + (d - 2 * a) // b
        if (d - 2 * a) % b != 0:
            tmp += 2
        result = min(result, tmp)
    print(result)
