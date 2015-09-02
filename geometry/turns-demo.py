import matplotlib.pyplot as plt
import numpy as np
import convexhullV2

if __name__ == "__main__":
    fig = plt.figure()
    fig.suptitle("Turn Orientation Demo", fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)

    ax.text(0, 19, 'Clockwise (Right Turn) Red')
    ax.text(0, 20, 'Counter-Clockwise (Left Turn) Blue')

    # Get 12 points of (x, y) where x, y are in the range [0, 20]
    points = np.random.rand(12, 2) * 20

    # Iterate over every 3 points
    for i in range(0, len(points), 3):
        triple = points[i:i+3]
        triple.sort(axis=0)

        # Plot in red if the triple make a clockwise turn, else blue
        if convexhullV2.cw_turn(triple):
            plt.plot([x[0] for x in triple], [x[1] for x in triple], "r-o")
        else:
            plt.plot([x[0] for x in triple], [x[1] for x in triple], "b-o")

    # Set axis limits
    plt.xlim(-1, 21)
    plt.ylim(-1, 21)

    plt.show()
