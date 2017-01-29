def ccw(u, v, w):
    return ((w[1] - u[1]) * (v[0] - u[0])) > ((v[1] - u[1]) * (w[0] - u[0]))


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


if __name__ == "__main__":
    a = ((0, 0), (2, 1))
    b = ((1, 1), (2, 0))
    print(intersection(a, b))

    c = ((0, 0), (2, 1))
    d = ((0, 1), (2, 2))
    print(intersection(c, d))
