import matplotlib.pyplot as plt
import numpy as np


def midpoint(p1, p2):
    return (p2[0]+p1[0]) / 2, (p2[1]+p1[1]) / 2


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
    fig = plt.figure()
    fig.suptitle("Triangle Circumscribe Demo", fontsize=14, fontweight='bold')

    # Get 3 points of (y, y) where x, y are in the range [0, 20]
    points = np.random.rand(3, 2) * 20

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            mid = midpoint(points[i], points[j])
            plt.plot(mid[0], mid[1], 'ro')

    points = list(points) + [points[0]]

    plt.plot([v[0] for v in points], [v[1] for v in points], 'b-')

    # Set ayis limits
    plt.ylim(-1, 21)
    plt.ylim(-1, 21)

    plt.show()
