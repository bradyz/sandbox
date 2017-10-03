import numpy as np
from scipy import linalg

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot(ax1, ax2, rest, vertices, neighbors, handles, scores):
    edges = get_edges(vertices, neighbors)
    handle_points = np.array(list(handles.values()))

    ax1.clear()
    ax1.set_axis_off()

    ax1.set_title('Point Visualization')
    # ax1.plot(edges[0], edges[1], edges[2], 'b--', linewidth=0.5)
    ax1.scatter(rest[:,0], rest[:,1], rest[:,2], 'g.')
    ax1.scatter(vertices[:,0], vertices[:,1], vertices[:,2], c='c')
    ax1.scatter(handle_points[:,0], handle_points[:,1], handle_points[:,2], c='r')

    ax2.set_title('Objective Function')
    ax2.plot(scores, 'r')

    plt.pause(0.01)


def make_R(c):
    return linalg.expm(make_Cx(c))


def make_Cx(c):
    return np.array([[  0.0, -c[2],  c[1]],
                     [ c[2],   0.0, -c[0]],
                     [-c[1],  c[0],  0.0]])


def energy(rest, vertices, c_list, neighbors, handles, alpha):
    result = 0.0

    for i, p_i_neighbors in neighbors.items():
        R = make_R(c_list[i])

        for j in p_i_neighbors:
            u = np.dot(R, rest[i] - rest[j])
            v = vertices[i] - vertices[j]

            result += sq_norm(u - v)

    for i, h_i in handles.items():
        result += alpha * sq_norm(vertices[i] - h_i)

    return result


def sq_norm(x):
    return np.inner(x, x)


def get_edges(vertices, neighbors):
    edges = [[], [], []]
    seen = set()

    for u, u_neighbors in neighbors.items():
        for v in u_neighbors:
            if (u, v) in seen:
                continue

            seen.add((u, v))

            for i in range(3):
                edges[i].append(vertices[u][i])
                edges[i].append(vertices[v][i])
                edges[i].append(float('NaN'))

    return edges


def initialize(n):
    rest = [[(i, j, 0.0) for j in range(n)] for i in range(n)]
    rest = np.array(rest).reshape((-1, 3))

    vertices = [[(i, j, 0.0) for j in range(n)] for i in range(n)]
    vertices = np.array(vertices).reshape((-1, 3))

    c_list = [np.array([1e-5, 1e-5, 1e-5]) for _ in range(n * n)]

    handles = {0: (0.0, 0.0, -0.5),
               n-1: (0.0, n-1, -0.5),
               (n // 2) * n + n // 2: (n // 2, n // 2, 1.0),
               (n-1) * n: (n-1, 0.0, -0.5),
               (n-1) * n + n-1: (n-1, n-1, -0.5)}

    for key, val in handles.items():
        handles[key] = np.array(val)

    triangles = list()

    for i in range(n):
        for j in range(n):
            a = (i-1, j-1)
            b = (i-1, j)
            c = (i, j-1)
            d = (i, j)

            skip = False

            for x in (a, b, c, d):
                if x[0] < 0 or x[1] < 0:
                    skip = True

            if skip:
                continue

            triangles.append((a, b, d))
            triangles.append((a, c, d))

    neighbors = dict()

    for a_b_c in triangles:
        for i in range(3):
            for j in range(i+1, 3):
                x = a_b_c[i][0] * n + a_b_c[i][1]
                y = a_b_c[j][0] * n + a_b_c[j][1]

                if x not in neighbors:
                    neighbors[x] = set()

                if y not in neighbors:
                    neighbors[y] = set()

                neighbors[x].add(y)
                neighbors[y].add(x)

    return rest, vertices, c_list, handles, neighbors


def get_dRdc(c):
    def get_dthetadci(i):
        return c[i] / theta

    def get_a(i):
        lhs = theta ** 2 * np.sin(theta) * get_dthetadci(i)
        rhs = -(1.0 - np.cos(theta)) * 2 * c[i]
        bot = theta ** 4

        return (lhs + rhs)

    def get_b(i):
        top = theta * np.cos(theta) - np.sin(theta) * get_dthetadci(i)
        bot = theta ** 2

        return top

    theta = np.linalg.norm(c)

    dRdcx_lhs = np.array([[0.0, c[1], c[2]],
                          [c[1], -2.0 * c[0], 0.0],
                          [c[2], 0.0, -2.0 * c[0]]])
    dRdcx_rhs = np.array([[0.0, 0.0, 0.0],
                          [0.0, 0.0, -1.0],
                          [0.0, 1.0, 0.0]])
    dRdcx = get_a(0) * dRdcx_lhs + get_b(0) * dRdcx_rhs

    dRdcy_lhs = np.array([[-2.0 * c[1], c[0], 0.0],
                          [c[0], 0.0, c[2]],
                          [0.0, c[2], -2.0 * c[1]]])
    dRdcy_rhs = np.array([[0.0, 0.0, 1.0],
                          [0.0, 0.0, 0.0],
                          [-1.0, 0.0, 0.0]])
    dRdcy = get_a(1) * dRdcy_lhs + get_b(1) * dRdcy_rhs

    dRdcz_lhs = np.array([[-2.0 * c[2],         0.0, c[0]],
                          [        0.0, -2.0 * c[2], c[1]],
                          [       c[0],        c[1], 0.0]])
    dRdcz_rhs = np.array([[0.0, -1.0, 0.0],
                          [1.0, 0.0, 0.0],
                          [0.0, 0.0, 0.0]])
    dRdcz = get_a(2) * dRdcz_lhs + get_b(2) * dRdcz_rhs

    return np.array([dRdcx.flatten(), dRdcy.flatten(), dRdcz.flatten()])


def get_dc(rest, vertices, c_list, neighbors):
    result = list()

    for i, p_i_neighbors in neighbors.items():
        c = c_list[i]
        R = make_R(c)

        dRdc = get_dRdc(c)
        dfdR = np.zeros((3, 3))

        for r in range(3):
            for c in range(3):
                for j in p_i_neighbors:
                    u = vertices[i] - vertices[j]
                    v = rest[i] - rest[j]

                    dfdR[r,c] += 2.0 * (np.dot(R[r,:], u) - v[r]) * u[c]

        dfdc = np.dot(dRdc, dfdR.flatten())

        result.append(dfdc)

    return result


def get_dp(rest, vertices, c_list, neighbors, handles, alpha):
    result = list()

    for i, p_i_neighbors in sorted(neighbors.items()):
        Ri = make_R(c_list[i])

        dp = np.zeros(3)

        for j in p_i_neighbors:
            Rj = make_R(c_list[j])

            dp += -2.0 * (np.dot(Ri, rest[i] - rest[j]) - (vertices[i] - vertices[j]))
            dp += 2.0 * (np.dot(Rj, rest[j] - rest[i]) - (vertices[j] - vertices[i]))

        if i in handles:
            dp += -2.0 * alpha * (handles[i] - vertices[i])

        result.append(np.copy(dp))

    return np.array(result)


def minimize(rest, vertices, c_list, neighbors, handles, alpha, h=4e-2):
    dcs = get_dc(rest, vertices, c_list, neighbors)
    dps = get_dp(rest, vertices, c_list, neighbors, handles, alpha)

    for i, dc in enumerate(dcs):
        c_list[i] =  c_list[i] - h * dc

    for i, dp in enumerate(dps):
        vertices[i] = vertices[i] - h * dp

    return vertices, c_list


def main(n=20, alpha=5.0):
    fig = plt.figure()

    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)

    rest, vertices, c_list, handles, neighbors = initialize(n)

    scores = list()

    while True:
        scores.append(
                energy(rest, vertices, c_list, neighbors, handles, alpha))

        plot(ax1, ax2, rest, vertices, neighbors, handles, scores)

        vertices, c_list = minimize(rest, vertices, c_list,
                                    neighbors, handles, alpha)


if __name__ == '__main__':
    np.random.seed(0)

    plt.ion()
    plt.show()

    main()
