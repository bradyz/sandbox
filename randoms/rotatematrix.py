def show(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))
    print()


def in_bounds(x, y, m, n):
    if x < m or x >= n:
        return False
    elif y < m or y >= n:
        return False
    return True


def perimeter(layer, n):
    x = layer
    y = layer

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        while in_bounds(x + dx, y + dy, layer, n - layer):
            x = x + dx
            y = y + dy
            yield x, y


def rotate(matrix, n):
    for i in range(n // 2):
        prev = matrix[i][i]

        for x, y in perimeter(i, n):
            matrix[x][y], prev = prev, matrix[x][y]


if __name__ == '__main__':
    n = 5
    matrix = [[n * i + j for j in range(n)] for i in range(n)]

    show(matrix)
    rotate(matrix, n)
    show(matrix)
