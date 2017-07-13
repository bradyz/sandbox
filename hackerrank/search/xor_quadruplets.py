def solve():
    result = a * b * c * d - a * c

    for i in range(1, a+1):
        for j in range(i+1, b+1):
            if c >= j and d >= j:
                result -= 4
            elif c >= i and c < j and d >= j:
                result -= 2
            else:
                break

    return result


a, b, c, d = map(int, input().split())

if a > b:
    a, b = b, a

if c > d:
    c, d = d, c

print(solve())
