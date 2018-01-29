def ccw(u, v, w):
    return ((w[1] - u[1]) * (v[0] - u[0])) >= ((v[1] - u[1]) * (w[0] - u[0]))


def intersection(a, b):
    """
    Returns true if the line segment a intersects the line segment b.

    Arguments:
        a: ((x1, y1), (x2, y2)), a 2D line segment.
        b: ((x3, y4), (x4, y4)), a 2D line segment.
    """
    p1, p2 = a
    p3, p4 = b
    return (ccw(p1, p3, p4) != ccw(p2, p3, p4) and
            ccw(p1, p2, p3) != ccw(p1, p2, p4))


def is_right_side(segment_a, three_point):
    for i in range(1, len(three_point)):
        a = three_point[i]
        b = three_point[i-1]

        if intersection((a, b), segment_a):
            return True

    return False


def dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def min_dist(a, players):
    dists = list()

    for i in range(5):
        x = players[2 * i]
        y = players[2 * i + 1]

        dists.append(dist(a, (x, y)))

    return min(dists)


point_n = int(input())
three_point = [list(map(int, input().split())) for _ in range(point_n)]
offense = list(map(int, input().split()))
defense = list(map(int, input().split()))
ball = list(map(int, input().split()))

players = list()

for i in range(5):
    x = offense[2 * i]
    y = offense[2 * i + 1]

    segment = ((x, y), (24, 0))

    is_on = is_right_side(segment, three_point) or point_n == 0
    player_dist = min_dist((x, y), defense)
    ball_dist = dist((x, y), ball)

    players.append((not is_on, -player_dist, ball_dist, i))

players.sort()

if players[0][0] == True:
    print(-1, -1)
else:
    winner = str(players[0][:-1])

    winners = [info[-1] for info in players if str(info[:-1]) == winner]
    coords = [(offense[2 * i], offense[2 * i + 1]) for i in winners]
    coords.sort()

    result = list()

    for c in coords:
        result.append(c[0])
        result.append(c[1])

    print(' '.join(map(str, result)))
