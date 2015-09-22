import matplotlib.pyplot as plt
from math import sqrt


def dist(a, b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def onclick(event):
    global points

    ix, iy = event.xdata, event.ydata

    if points and dist((ix, iy), points[0]) < .5:
        plt.plot([points[-1][0], points[0][0]],
                 [points[-1][1], points[0][1]], "-")
    else:
        # points.append(("%.3f" % ix, "%.3f" % iy))
        points.append((ix, iy))

        plt.plot([c[0] for c in points[-2:]], [c[1] for c in points[-2:]], "-")
        plt.plot(ix, iy, "ro")

    ax.get_figure().canvas.draw()

points = []

fig = plt.figure()
ax = fig.add_subplot(111)
cid = fig.canvas.mpl_connect('button_press_event', onclick)

plt.xlim(-10, 10)
plt.ylim(-10, 10)

plt.show()
