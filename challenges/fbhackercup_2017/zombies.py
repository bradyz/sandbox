BOX = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


def inside(min_x, max_x, min_y, max_y, points):
    result = set()

    for i in range(len(points)):
        x, y = points[i]
        if x >= min_x and x <= max_x and y >= min_y and y <= max_y:
            result.add(i)

    return result


def solve(n, r, c):
    all_boxes = list()

    for x, y in c:
        for dx, dy in BOX:
            nx = x + r * dx
            ny = y + r * dy

            min_x = min(x, nx)
            max_x = max(x, nx)

            min_y = min(y, ny)
            max_y = max(y, ny)

            all_boxes.append(inside(min_x, max_x, min_y, max_y, c))

    result = 0

    for i in range(len(all_boxes)):
        for j in range(i+1, len(all_boxes)):
            result = max(result, len(all_boxes[i] | all_boxes[j]))

    return result


for i in range(1, int(input())+1):
    n, r = map(int, input().split())
    c = [list(map(int, input().split())) for _ in range(n)]
    print("Case #%d: %d" % (i, solve(n, r, c)))
