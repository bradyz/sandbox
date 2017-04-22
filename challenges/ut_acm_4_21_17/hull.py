def subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])


def cross(u, v):
    return (0, 0, u[0] * v[1] - u[1] * v[0])


def is_positive(p1, p2, p3, q):
    u = subtract(q, p1)
    v = subtract(p2, p1)
    x = cross(u, v)
    if x[2] > 0:
        return 1
    return 0


for _ in range(int(input())):
    values = list(map(int, input().split()))
    points = list()

    for i in range(0, len(values), 2):
        x, y = values[i], values[i+1]
        points.append((x, y))

    result = False

    for i in range(4):
        for j in range(i+1, 4):
            for k in range(j+1, 4):
                p1 = points[i]
                p2 = points[j]
                p3 = points[k]
                q = points[6 - i - j - k]

                triangle = [p1, p2, p3]

                signs = list()

                for x in range(3):
                    a = triangle[x]
                    b = triangle[(x+1) % 3]
                    c = triangle[(x+2) % 3]

                    signs.append(is_positive(a, b, c, q))

                if sum(signs) == 0 or sum(signs) == 3:
                    result = True

    if result:
        print("YES")
    else:
        print("NO")
