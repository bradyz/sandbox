import numpy as np
import matplotlib.pyplot as plt


def norm_sq(P):
    return np.linalg.norm(P, 'fro') ** 2


def energy(A, G, B, C, mu):
    return norm_sq(G * (A - np.dot(B, C))) + mu / 2.0 * (norm_sq(B) + norm_sq(C))


def get_dB(A, G, B, C, mu, i):
    n, r = B.shape

    result = mu * B[i].T

    for k in range(n):
        result += -2.0 * G[i,k] * (A[i,k] - np.dot(B[i], C[:,k])) * C[:,k]

    return result


def get_dC(A, G, B, C, mu, i):
    r, n = C.shape

    result = mu * C[:,i]

    for k in range(n):
        result += -2.0 * G[k,i] * (A[k,i] - np.dot(B[k], C[:,i])) * B[k].T

    return result


def get_ddBii(A, G, B, C, mu, i):
    n, r = B.shape

    result = mu * np.eye(r)

    for k in range(n):
        result += 2.0 * G[i,k] * np.outer(C[:,k], C[:,k].T)

    return result


def get_ddCii(A, G, B, C, mu, i):
    r, n = C.shape

    result = mu * np.eye(r)

    for k in range(n):
        result += 2.0 * G[k,i] * np.outer(B[k].T, B[k])

    return result


def get_ddBiCj(A, G, B, C, mu, i, j):
    n, r = B.shape

    result = 2.0 * G[i,j] * (
            (np.dot(C[:,j].T, B[i].T) - A[i,j]) * np.eye(r) +
            np.outer(B[i].T, C[:,j].T))

    return result


def get_gradient(A, G, B, C, mu):
    n, r = B.shape

    result = np.zeros((2 * n * r))

    for i in range(2 * n):
        si = r * i

        block = None

        if i < n:
            block = get_dB(A, G, B, C, mu, i)
        else:
            block = get_dC(A, G, B, C, mu, i-n)

        result[si:si+r] = block

    return result


def get_hessian(A, G, B, C, mu):
    n, r = B.shape

    result = np.zeros((2 * n * r, 2 * n * r))

    for i in range(2 * n):
        for j in range(2 * n):
            si = r * i
            sj = r * j

            block = None

            if i == j and i < n:
                block = get_ddBii(A, G, B, C, mu, i)
            elif i == j and i >= n:
                block = get_ddCii(A, G, B, C, mu, i-n)
            elif i < n and j >= n:
                block = get_ddBiCj(A, G, B, C, mu, i, j-n)
            elif i >= n and j < n:
                block = get_ddBiCj(A, G, B, C, mu, j, i-n).T

            if block is not None:
                result[si:si+r,sj:sj+r] = block

    return result


def solve_dBi(A, G, B, C, mu, k):
    n, r = B.shape

    A_ = mu * np.eye(r)

    for j in range(n):
        A_ += 2.0 * G[k,j] * np.outer(C[:,j], C[:,j].T)

    b_ = np.zeros((r))

    for j in range(n):
        b_ += 2.0 * G[k,j] * A[k,j] * C[:,j]

    return np.linalg.solve(A_, b_)


def solve_dCi(A, G, B, C, mu, k):
    r, n = C.shape

    A_ = mu * np.eye(r)

    for i in range(n):
        A_ += 2.0 * G[i,k] * np.outer(B[i].T, B[i])

    b_ = np.zeros((r))

    for i in range(n):
        b_ += 2.0 * G[i,k] * A[i,k] * B[i].T

    return np.linalg.solve(A_, b_)


def best_B(A, G, B, C, mu):
    n, r = B.shape

    result = np.zeros((n, r))

    for i in range(n):
        result[i] = solve_dBi(A, G, B, C, mu, i)

    return result


def best_C(A, G, B, C, mu):
    r, n = C.shape

    result = np.zeros((r, n))

    for i in range(n):
        result[:,i] = solve_dCi(A, G, B, C, mu, i)

    return result


def alternating_minimization(A, G, B, C, mu, max_iterations=100):
    values = list()

    for i in range(max_iterations):
        if i == 50:
            import pdb; pdb.set_trace()

        track_results(A, G, B, C, mu, values)

        if i % 2 == 0:
            B = best_B(A, G, B, C, mu)
        else:
            C = best_C(A, G, B, C, mu)


def get_best_step(g, H, delta):
    p = -delta * g / np.linalg.norm(g)

    b_norm = np.dot(g.T, np.dot(H, g))

    if b_norm <= 0.0:
        tau = 1.0
    else:
        top = np.linalg.norm(g) ** 3
        bot = delta * b_norm

        tau = min(1.0, top / bot)

    return tau * p


def alter_B(B, g):
    n, r = B.shape

    result = np.copy(B)

    for i in range(n):
        result[i] += g[i*r:i*r+r]

    return result


def alter_C(C, g):
    r, n = C.shape

    result = np.copy(C)

    for i in range(n, 2 * n):
        result[:,i-n] += g[i*r:i*r+r]

    return result


def approx(p, g, H):
    return -(np.dot(g, p) + 0.5 * np.dot(p.T, np.dot(H, p)))


def trust_region(A, G, B, C, mu,
                 eta=0.25,
                 delta=0.05, max_delta=2.0,
                 max_iterations=100):
    values = list()

    for i in range(max_iterations):
        if i == 50:
            import pdb; pdb.set_trace()

        track_results(A, G, B, C, mu, values)

        g = get_gradient(A, G, B, C, mu)
        H = get_hessian(A, G, B, C, mu)

        try:
            assert np.all(H.T == H)
            assert np.sum(np.isnan(H)) == 0
        except:
            import pdb; pdb.set_trace()

        p_k = get_best_step(g, H, delta)

        B_prime = alter_B(B, p_k)
        C_prime = alter_C(C, p_k)

        top = energy(A, G, B, C, mu) - energy(A, G, B_prime, C_prime, mu)
        bot = approx(p_k, g, H)

        rho = top / bot

        if rho < 0.25:
            delta = 0.25 * delta
        else:
            if rho > 0.75 and abs(np.linalg.norm(p_k) - delta) < 1e-5:
                delta = min(2.0 * delta, max_delta)

        print(np.linalg.norm(p_k))

        if rho >= eta:
            B = B_prime
            C = C_prime


def track_results(A, G, B, C, mu, values):
    value = energy(A, G, B, C, mu)
    values.append(value)

    AG = A * G
    BC = G * np.dot(B, C)

    min_val = min(np.min(AG), np.min(BC))
    max_val = max(np.max(AG), np.max(BC))

    AG = (AG - min_val) / (max_val - min_val)
    BC = (BC - min_val) / (max_val - min_val)

    plt.subplot(2, 2, 1)
    plt.title('Current Energy: %.3f' % value)
    plt.xlabel('Iterations')
    plt.ylabel('Energy (Log)')
    plt.plot(np.log(values), color='b', marker='.', linestyle='-')

    plt.subplot(2, 2, 3)
    plt.title('G * A')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(AG, interpolation='None')

    plt.subplot(2, 2, 4)
    plt.title('G * BC')
    plt.xticks([])
    plt.yticks([])
    plt.imshow(BC, interpolation='None')

    plt.pause(1e-3)


def main(n, r, sparsity=0.05, mu=0.1):
    A = np.random.rand(n, n)
    G = np.float32(np.random.rand(n, n) < sparsity)

    B = np.random.rand(n, r)
    C = np.random.rand(r, n)

    # alternating_minimization(A, G, B, C, mu)
    trust_region(A, G, B, C, mu)


if __name__ == '__main__':
    np.random.seed(0)

    plt.ion()
    plt.show()

    main(25, 5)
