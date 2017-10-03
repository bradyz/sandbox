import numpy as np

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def plot(ax1, ax2, rest, vertices, neighbors, handles, scores):
    edges = get_edges(vertices, neighbors)
    handle_points = np.array(list(handles.values()))

    ax1.clear()

    ax1.set_title('Point Visualization')
    ax1.plot(edges[0], edges[1], edges[2], 'c--', linewidth=0.5)
    ax1.scatter(rest[:,0], rest[:,1], rest[:,2], 'g.')
    ax1.scatter(vertices[:,0], vertices[:,1], vertices[:,2], 'b.')
    ax1.scatter(handle_points[:,0], handle_points[:,1], handle_points[:,2], 'r.')

    ax2.set_title('Objective Function')
    ax2.plot(scores, 'r')

    plt.pause(0.01)


def energy(rest, vertices, rotations, neighbors, handles, alpha):
    result = 0.0

    for i, p_i_neighbors in neighbors.items():
        for j in p_i_neighbors:
            u = np.dot(rotations[i], (rest[i] - rest[j]))
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


def initialize(n, dz=0.5):
    rest = [[(i, j, 0.0) for j in range(n)] for i in range(n)]
    rest = np.array(rest).reshape((-1, 3))

    vertices = [[(i, j, 0.0) for j in range(n)] for i in range(n)]
    vertices = np.array(vertices).reshape((-1, 3))

    rotations = [np.eye(3) for _ in range(n * n)]

    handles = {0: (0.0, 0.0, -1.0),
               n-1: (0.0, n-1, -1.0),
               (n // 2) * n + n // 2: (n // 2, n // 2, 0.5),
               (n-1) * n: (n-1, 0.0, -1.0),
               (n-1) * n + n-1: (n-1, n-1, -1.0)}

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

    return rest, vertices, rotations, handles, neighbors


def min_vertices(rest, vertices, rotations, neighbors, handles, alpha):
    n = len(neighbors)

    block_A = list()
    block_b = list()

    for i, p_i_neighbors in neighbors.items():
        for j in p_i_neighbors:
            A = np.zeros((3, n * 3))
            A[:,3*i:3*i+3] = np.eye(3)
            A[:,3*j:3*j+3] = -np.eye(3)

            block_A.append(A)

            p_i_rest = rest[i]
            p_j_rest = rest[j]

            block_b.append(np.dot(rotations[i], (p_i_rest - p_j_rest)))

    for i, handle_i in handles.items():
        A = np.zeros((3, n * 3))
        A[:,3*i:3*i+3] = np.sqrt(alpha) * np.eye(3)

        block_A.append(A)
        block_b.append(np.sqrt(alpha) * handle_i)

    A = np.array(block_A).reshape((-1, 3 * n))
    b = np.array(block_b).flatten()

    x = np.dot(np.linalg.inv(np.dot(A.T, A)), np.dot(A.T, b))

    return x.reshape((-1, 3))


def min_rotations(rest, vertices, rotations, neighbors):
    result = [None for _ in rotations]

    for i, p_i_neighbors in neighbors.items():
        block_P = list()
        block_Q = list()

        for j in p_i_neighbors:
            p_i_rest = rest[i]
            p_j_rest = rest[j]

            p_i = vertices[i]
            p_j = vertices[j]

            block_P.append(p_i_rest - p_j_rest)
            block_Q.append(p_i - p_j)

        P = np.array(block_P).T
        Q = np.array(block_Q).T

        U, _, V = np.linalg.svd(np.dot(P, Q.T))

        result[i] = np.dot(V, U.T)

        if np.linalg.det(result[i]) == -1:
            S = np.eye(3)
            S[2][2] = -1.0

            result[i] = np.dot(V, np.dot(S, U.T))

    return result


def minimize(rest, vertices, rotations, neighbors, handles, alpha):
    vertices = min_vertices(rest, vertices, rotations,
                            neighbors, handles, alpha)
    rotations = min_rotations(rest, vertices, rotations, neighbors)

    return vertices, rotations


def main(n=21, alpha=1.0):
    fig = plt.figure()

    ax1 = fig.add_subplot(121, projection='3d')
    ax2 = fig.add_subplot(122)

    rest, vertices, rotations, handles, neighbors = initialize(n)

    scores = list()

    while True:
        scores.append(
                energy(rest, vertices, rotations, neighbors, handles, alpha))

        plot(ax1, ax2, rest, vertices, neighbors, handles, scores)

        vertices, rotations = minimize(rest, vertices, rotations,
                                       neighbors, handles, alpha)


if __name__ == '__main__':
    np.random.seed(0)

    plt.ion()
    plt.show()

    main()
