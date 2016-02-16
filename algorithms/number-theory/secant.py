from math import sin, cos, exp, log


def problem1(x):
    return x ** 2 - 6


def problem2(x):
    return - x ** 3 - cos(x)


def problem3(x):
    return exp(x) + 2 ** (-x) + 2 * cos(x) - 6


def problem3p(x):
    return exp(x) - ((2 ** (-x)) * log(2)) + 2 * - sin(x)


def problem4(x):
    return x ** 2 - 4 * x + 4 - log(x)


def newton(f, fp, p0, eps=0, iterations=100):
    for i in range(1, iterations+1):
        p = p0 - f(p0) / fp(p0)

        print("i: " + str(i) + "\tp: %.9f\t\tf(p): %.9f\t\teps: %.9f"
              % (p, f(p0), abs(p-p0)))

        if abs(p - p0) < eps:
            return p

        p0 = p

    return None


def secant(f, p0, p1, eps=0, iterations=100):
    q0 = f(p0)
    q1 = f(p1)

    for i in range(2, iterations+1):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        print("i: " + str(i) + "\tp: %.9f\t\tf(p): %.9f\t\teps: %.9f"
              % (p, f(p), abs(p-p1)))

        if abs(p - p1) < eps:
            return p

        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p)

    return None


if __name__ == "__main__":
    print("problem 1")
    secant(problem1, 3, 2, 0, 3)

    print("\nproblem 2")
    secant(problem2, -1, 0, 0, 3)

    print("\nproblem 3")
    newton(problem3, problem3p, 1.5, 1e-6)

    print("\nproblem 4")
    secant(problem4, 2, 4, 1e-7)
