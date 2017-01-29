class Pt():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def ccw(A, B, C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)


def intersection(a, b):
    x1, y1 = a
    x2, y2 = b
    A = Pt(a[0][0], a[0][1])
    B = Pt(a[1][0], a[1][1])
    C = Pt(b[0][0], b[0][1])
    D = Pt(b[1][0], b[1][1])
    return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)


n, m = map(int, input().split())
segments = list()
for _ in range(n):
    time = 0
    positions = list(map(int, input().split()[1:]))
    current = list()
    for i in range(1, len(positions)):
        x1, y1 = time, positions[i-1]
        x2, y2 = time + abs(positions[i] - positions[i-1]), positions[i]
        current.append(((x1, y1), (x2, y2)))
        time += abs(positions[i] - positions[i-1])
    segments.append(current)

for _ in range(m):
    u, v = map(int, input().split())
    r = 0
    for i in range(len(segments[u-1])):
        for j in range(len(segments[v-1])):
            if intersection(segments[u-1][i], segments[v-1][j]):
                r += 1
    print(r)
