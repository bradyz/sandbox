import matplotlib.pyplot as plt

if __name__ == "__main__":
    fig = plt.figure()

    W, H = map(int, input().split())

    # plot all points to be valid
    for i in range(W):
        for j in range(H):
            plt.plot([i], [j], "go")

    # graves
    for _ in range(int(input())):
        x, y = map(int, input().split())
        plt.plot(x, y, "ro")

    # portals
    for _ in range(int(input())):
        x1, y1, x2, y2, t = map(int, input().split())
        plt.text((x1+x2) / 2, (y1+y2) / 2, str(t))
        plt.plot([x1, x2], [y1, y2], "g--")

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
