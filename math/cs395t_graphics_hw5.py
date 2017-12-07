import numpy as np
import scipy.optimize


EPS = 1e-9


def simplex_method_slow(c, A, b, m, n, n_iterations=1000):
    basic = [i for i in range(n - m, n)]
    non_basic = [i for i in range(n - m)]

    B = np.array([A[:,i] for i in basic]).T
    N = np.array([A[:,i] for i in non_basic]).T

    x_b = np.dot(np.linalg.inv(B), b)

    for iteration in range(n_iterations):
        c_b = np.array([c[i] for i in basic])
        c_n = np.array([c[i] for i in non_basic])

        s_n = c_n - np.dot(N.T, np.linalg.solve(B.T, c_b))

        indices = [i for i in range(m) if s_n[i] < 0.0]

        if not indices:
            z = sum([c[basic[i]] * x_b[i] for i in range(len(basic))])

            return np.array([x_b[basic.index(i)] if i in basic else 0.0 for i in range(n)]), z

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


def interior_point_method_slow(c, A, b, m, n, sig=0.1, a=1e-1, n_iterations=1000):
    x = np.random.rand(n)
    s = np.random.rand(n)
    l = np.random.rand(m)

    for iteration in range(n_iterations):
        mu = np.dot(x.T, s) / n

        A_prime = np.zeros((n + m + n, n + m + n))
        A_prime[:n,n:n+m] = A.T
        A_prime[:n,n+m:] = np.eye(n)
        A_prime[n:n+m,:n] = A
        A_prime[n+m:,:n] = np.diag(s)
        A_prime[n+m:,n+m:] = np.diag(x)

        b_prime = np.zeros(n + m + n)
        b_prime[:n] = -(np.dot(A.T, l) + s - c)
        b_prime[n:n+m] = -(np.dot(A, x) - b)
        b_prime[n+m:] = -(x * s * np.ones(n) + sig * mu * np.ones(n))

        x_prime = np.linalg.solve(A_prime, b_prime)
        dx = x_prime[:n]
        dl = x_prime[n:n+m]
        ds = x_prime[n+m:]

        x += a * dx
        l += a * dl
        s += a * ds

    x[np.abs(x)<1e-10] = 0.0

    return x, np.dot(x, c)


def toy():
    m = 2
    n = 4

    c = np.float32([-4, -2, 0, 0])

    A = np.float32([
        [1, 1, 1, 0],
        [2, 0.5, 0, 1]
        ])
    b = np.float32([5, 8])

    return c, A, b, m, n


def big():
    m = 100
    n = 200

    c = np.random.rand(n) - 0.5
    c[m:] = 0.0

    A = np.random.rand(m, n)
    A[:,m:] = np.diag(np.ones(m))

    b = np.random.rand(m)

    return c, A, b, m, n


def test(func):
    c, A, b, m, n = func()

    solution = scipy.optimize.linprog(c, A_eq=A, b_eq=b)

    x_solution = solution.x
    z_solution = solution.fun

    x_ipm, z_ipm = interior_point_method_slow(c, A, b, m, n)
    x_simp, z_simp = simplex_method_slow(c, A, b, m, n)

    print(x_solution, z_solution)
    print(x_ipm, z_ipm)
    print(x_simp, z_simp)
    print()


def main():
    test(toy)
    test(big)


if __name__ == '__main__':
    np.random.seed(0)

    main()
