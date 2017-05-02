import sys
from matplotlib import pyplot as plt


def graph(points):
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.xlim([min(x), max(x)])
    plt.ylim([min(y), max(y)])

    plt.plot(x, y, ".")

    plt.show()


if __name__ == '__main__':
    graph([tuple(map(float, line.split())) for line in sys.stdin])
