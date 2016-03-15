from matplotlib import pyplot as plt


def de_boor(t, points, n):
    u = [points[0]] * 2 + points + [points[-1]] * 2

    u_i_1 = 2+n
    for i in range(2, 2+n):
        if u[i][0] > t:
            u_i_1 = i
            break

    a = [[0 for _ in range(6)] for _ in range(6)]
    p = [[u[i][1] for i in range(u_i_1-3, u_i_1+3)] for _ in range(3)]
    u = [x[0] for x in u]

    for r in range(1, 3):
        for i in range(k-p+r, k-s):
            a[i][r] = (t - u[i]) / (u[i+p-r+1] - u[i])
            p[i][r] = (1-a[i][r]) * p[i-1][r-1] + a[i][r] * p[i][r-1]

    print(u_i_1)
    print(t)
    print("\n".join(map(str, p)))
    print(u_i_1, u[u_i_1])


if __name__ == "__main__":
    n = int(input())
    point = [list(map(int, input().split())) for _ in range(n)]

    x_c = [x[0] for x in point]
    y_c = [x[1] for x in point]
    plt.plot(x_c, y_c, "-")
    plt.plot(x_c, y_c, "ro")

    de_boor(0, point, n)
    de_boor(5, point, n)

    # plt.show()
