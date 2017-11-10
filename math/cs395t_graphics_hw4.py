import numpy as np
import matplotlib.pyplot as plt

from scipy.io import loadmat


def l1(x):
    return np.linalg.norm(x, 1)


def l2_squared(x):
    return np.linalg.norm(x, 2) ** 2


def score(A_list, x_list, b_list, reg):
    score = 0.0

    for A, x, b in zip(A_list, x_list, b_list):
        score += l2_squared(np.dot(A, x) - b)

    for i in range(len(x_list)):
        for j in range(i+1, len(x_list)):
            score += reg * l1(x_list[i] - x_list[j])

    return score


def get_gradients(A_list, x_list, b_list):
    dx_list = list()

    for A, x, b in zip(A_list, x_list, b_list):
        dx_list.append(np.dot(A.T, np.dot(A, x) - b))

    return dx_list


def solve_single(x_l, reg, old_to_new):
    n = len(x_l)

    for i in range(1, n):
        if x_l[i][0] != x_l[i-1][0]:
            continue

        for j in old_to_new:
            if old_to_new[j] >= i:
                old_to_new[j] -= 1

        x_l.pop(i)

        return solve_single(x_l, reg, old_to_new)

    u_list = list()

    for k in range(n):
        u_k = x_l[k][0]

        for i in range(k):
            u_k -= reg * x_l[i][1]

        for i in range(k+1, n):
            u_k += reg * x_l[i][1]

        u_list.append(u_k)

        if len(u_list) >= 2 and u_list[-2] >= u_list[-1]:
            x_i, c_i = x_l[k]
            x_j, c_j = x_l[k-1]

            value = (c_i * x_i + c_j * x_j) / (c_i + c_j)

            x_l[k-1] = [value, c_i + c_j]
            x_l[k] = [value, None]

            return solve_single(x_l, reg, old_to_new)

    return u_list


def get_prox(x_list, reg):
    d = x_list[0].shape[0]

    u_list = [np.zeros(d) for x in x_list]

    for i in range(d):
        xs = [x[i] for x in x_list]

        # Sorted by value.
        x_old_index = [(x, old_index) for old_index, x in enumerate(xs)]
        x_old_index.sort()

        old_to_new = {old: new for new, (_, old) in enumerate(x_old_index)}
        x_l = [[x, xs.count(x)] for x, _ in x_old_index]

        us = solve_single(x_l, reg, old_to_new)

        for j in range(len(x_list)):
            u_list[j][i] = us[old_to_new[j]]

    return u_list


def optimize(A_list, x_list, b_list, reg=1.0, h=1e-2, max_iterations=1000):
    scores = list()

    for iteration in range(max_iterations):
        scores.append(score(A_list, x_list, b_list, reg))

        plt.title('Current Value: %.2f' % scores[-1])
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function')
        plt.plot(list(range(len(scores))), scores, 'r-o')
        plt.pause(0.01)

        dx_list = get_gradients(A_list, x_list, b_list)

        for i in range(len(x_list)):
            x_list[i] -= h * dx_list[i]

        x_list = get_prox(x_list, h * reg)


def main():
    np.random.seed(0)

    plt.ion()
    plt.show(block=False)

    data = loadmat('hw4_data.mat')

    A_list = np.squeeze(data['A'])
    b_list = [np.squeeze(b) for b in np.squeeze(data['b'])]

    # x_list = [np.random.rand(A_list[0].shape[1]) for _ in b_list]
    # x_list = [np.zeros(A_list[0].shape[1]) for _ in b_list]
    x_list = [np.linalg.lstsq(A, b)[0] for A, b in zip(A_list, b_list)]

    optimize(A_list, x_list, b_list)


if __name__ == '__main__':
    main()
