import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig = plt.figure()
    ax = plt.axes()

    W, H = map(int, input().split())

    # plot all points to be valid
    for i in range(W):
        for j in range(H):
            plt.plot([i], [j], "go")

    # graves
    for _ in range(int(input())):
        x, y = map(int, input().split())
        plt.plot(x, y, "ro")

    quivers = list()

    # portals
    for _ in range(int(input())):
        x1, y1, x2, y2, t = map(int, input().split())
        plt.text((x1+x2) / 2, (y1+y2) / 2, str(t))
        plt.plot([x1, x2], [y1, y2], "g--")
        quivers.append((x1, y1, (x2-x1)/2, (y2-y1)/2))

    plt.quiver([a[0] for a in quivers], [b[1] for b in quivers],
               [c[2] for c in quivers], [d[3] for d in quivers], scale=5)

    # boundaries
    plt.plot([-1, W, W, -1, -1], [-1, -1, H, H, -1], "b--")

    # start, goal is cyan dot
    plt.plot([W-1], [H-1], "co")

    # start, goal is cyan dot
    plt.plot([0], [0], "co")

    # make sure you see the whole map
    plt.ylim([-2, H+2])
    plt.xlim([-2, W+2])

    plt.show()
