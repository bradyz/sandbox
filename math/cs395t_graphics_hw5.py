import numpy as np
import scipy.optimize


EPS = 1e-9


def solve(c, A, b, m, n, max_iterations=100000):
    basic = [i for i in range(n - m, n)]
    non_basic = [i for i in range(n - m)]

    B = np.array([A[:,i] for i in basic]).T
    N = np.array([A[:,i] for i in non_basic]).T

    x_b = np.dot(np.linalg.inv(B), b)

    for iteration in range(max_iterations):
        c_b = np.array([c[i] for i in basic])
        c_n = np.array([c[i] for i in non_basic])

        s_n = c_n - np.dot(N.T, np.linalg.solve(B.T, c_b))

        indices = [i for i in range(m) if s_n[i] < 0.0]

        if not indices:
            z = sum([c[basic[i]] * x_b[i] for i in range(len(basic))])

            print('solution')
            import pdb; pdb.set_trace()
            return

        q = non_basic[indices[0]]
        d = np.linalg.solve(B, A[:,q])

        if np.all(d < 0.0):
            return 'UNBOUNDED'

        ratios = [(x_b[i] / d[i], i) for i in range(m) if d[i] > 0.0]
        x_q_prime, p = min(ratios, key=lambda x: x[0])

        x_b_prime = x_b - d * x_q_prime
        x_b_prime[p] = x_q_prime

        p = basic[p]

        basic[basic.index(p)] = q
        non_basic[non_basic.index(q)] = p

        x_b = x_b_prime

        B = np.array([A[:,i] for i in basic]).T
        N = np.array([A[:,i] for i in non_basic]).T


def main():
    m = 2
    n = 4

    c = np.float32([-4, -2, 0, 0])

    A = np.float32([
        [1, 1, 1, 0],
        [2, 0.5, 0, 1]
        ])
    b = np.float32([5, 8])

    solve(c, A, b, m, n)

    m = 100
    n = 200

    c = np.random.rand(n) - 0.5
    c[m:] = 0.0
    A = np.random.rand(m, n)
    A[:,m:] = np.diag(np.ones(m))
    b = np.random.rand(m)

    print(scipy.optimize.linprog(c, A_eq=A, b_eq=b))

    solve(c, A, b, m, n)


if __name__ == '__main__':
    np.random.seed(0)

    main()
