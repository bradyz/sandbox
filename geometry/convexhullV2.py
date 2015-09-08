def det(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])


def colinear(points):
    return det(*sorted(points, key=lambda x: x[0])) == 0


def cw_turn(points):
    return det(*sorted(points, key=lambda x: x[0])) < 0


def ccw_turn(points):
    return not cw_turn(points) and not colinear(points)


# Graham Scan O(nlogn)
def convex_hull(points):
    # lower or upper hull
    def lu_hull(points, is_upper=True):
        points = list(sorted(points, key=lambda x: x[0]))   # Sorted by x
        hull = [points[0], points[1]]

        # Calculating upper hull checks if the points do NOT make a right turn
        if is_upper:
            turn = cw_turn
        else:
            turn = ccw_turn

        for pi in points[2:]:
            hull.append(pi)

            # Check the last three points do not make a left/right turn
            while len(hull) > 2 and not turn(hull[-3:]):
                hull.pop(-2)

        return hull

    # Return the lower and upper hull
    return lu_hull(points) + list(reversed(lu_hull(points, False)))
