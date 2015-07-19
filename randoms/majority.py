a = [1, 2, 3, 1, 1, 5, 6, 1, 7, 1, 1, 1]
b = [1, 2, 3, 1, 1]


def solve(c):
    x = 0
    y = 0
    i = 0

    while i < len(c):
        if c[i] == c[x]:
            y += 1
        else:
            y -= 1

        if y < 0:
            x = i
            y = 0

        i += 1

    print(c[x], x, y)

solve(a)
solve(b)
