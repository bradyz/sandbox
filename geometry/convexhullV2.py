import math
import numpy as np


def det(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1])-(c[0]-a[0])*(b[1]-a[1])


def cw_turn(points):
    return det(*points) < 0


def ccw_turn(points):
    return det(*points) > 0


def colinear(points):
    return det(*points) == 0


def upper_hull(points):
    return 0


def lower_hull(points):
    return 0


def convex_hull(points):
    lower = lower_hull(points)
    upper = upper_hull(points)
    return lower+upper
