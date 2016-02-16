def problem1(x):
    return x ** 2 - 6


def secant(f, p0, p1, eps=0, iterations=100):
    q0 = f(p0)
    q1 = f(p1)

    for i in range(2, iterations+1):
        p = p1 - q1 * (p1 - p0) / (q1 - q0)

        print("i: " + str(i) +
              "\tp: " + str(p) +
              "\tf(p): " + str(f(p)) +
              "\teps: " + str(abs(p-p1)))

        if abs(p - p1) < eps:
            return p

        p0 = p1
        p1 = p
        q0 = q1
        q1 = f(p)


if __name__ == "__main__":
    print("problem 1")
    secant(problem1, 3, 2, 0, 3)
