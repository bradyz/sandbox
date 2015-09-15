import matplotlib.pyplot as plt
import numpy as np
import math


def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)


def midpoint(p1, p2):
    return (p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2


def slope(p1, p2):
    return (p2[1] - p1[1]) / (p2[0] - p1[0])


def perpendicular(m):
    return (0 == m and m) or -1 / m


def anotherpoint(p1, m, off):
    return p1[0] + off, p1[1] + m*off


def line(p1, p2):
    A = p1[1] - p2[1]
    B = p2[0] - p1[0]
    C = p1[0]*p2[1] - p2[0]*p1[1]
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


if __name__ == "__main__":
    # Configure graph and add title
    fig = plt.figure()
    fig.suptitle("Triangle Circumscribe Demo", fontsize=14, fontweight='bold')

    # Get 3 points of (y, y) where x, y are in the range [0, 20]
    points = np.random.rand(3, 2) * 20

    # List of perpendicular bisectors
    bisectors = []

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # Find the biscector and the inverse slope of the line
            mid = midpoint(points[i], points[j])
            perp = perpendicular(slope(points[i], points[j]))

            # Finds two points on the perpendicular line for plotting
            ap1 = anotherpoint(mid, perp, off=100)
            ap2 = anotherpoint(mid, perp, off=-100)

            # Save the bisectors for later to find the intersecting point
            bisectors.append((ap1, ap2))

            # Plot the perpendicular bisector
            plt.plot([ap1[0], ap2[0]], [ap1[1], ap2[1]], 'g--')

    # The point at which the bisectors intersect
    center = intersection(line(*bisectors[0]), line(*bisectors[1]))

    # Plot the center of the triangle
    plt.plot(center[0], center[1], 'ro')

    # Create the circle at center with a radius the distance to any point
    circle = plt.Circle((center[0], center[1]), distance(center, points[0]),
                        color='r', fill=False)

    # Add circle to graph
    fig = plt.gcf()
    fig.gca().add_artist(circle)

    # Append the beginning of the list so it creates a polygon
    points = list(points) + [points[0]]

    # Plot the random points
    plt.plot([v[0] for v in points], [v[1] for v in points], 'b-')

    # Set ayis limits
    plt.ylim(-21, 41)
    plt.xlim(-21, 41)

    plt.show()
