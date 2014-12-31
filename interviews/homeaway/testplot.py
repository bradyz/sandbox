import matplotlib.pyplot as plt

if __name__ == "__main__":
    with open('testplot-input.txt', 'r') as f:
        lines = f.readlines()

    for l in lines:
        a = l.split()

        x = []
        y = []

        for coor in a:
            xy = coor.split(',')
            x.append(xy[0])
            y.append(xy[1])

        print x
        print y

    plt.plot(x, y, 'ro')
    plt.show()
