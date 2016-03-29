from math import cos, sin, exp


# a, b endpoints, n even
def compsimpson(f, a, b, n):
    h = (b - a) / n
    x_even = 0
    x_odd = 0
    for i in range(1, n, 2):
        x_odd += f(a + i * h)
    for i in range(2, n, 2):
        x_even += f(a + i * h)
    return (h / 3) * (f(a) + 2 * x_even + 4 * x_odd + f(b))


def comptrapezoidal(f, a, b, n):
    h = (b - a) / n
    middle = sum(f(a + i * h) for i in range(1, n))
    return (h / 2) * (f(a) + 2 * middle + f(b))


def rhomberg(f, a, b, n):
    h = b - a
    r = [[0 for _ in range(n)] for _ in range(2)]
    r[0][0] = (h / 2) * (f(a) + f(b))
    ret = list()
    print("n:", 1, "%.8f" % r[0][0])
    ret.append("r[1][1]: " + str(r[0][0]))
    for i in range(2, n+1):
        r[1][0] = .5 * (r[0][0] + h * sum(f(a + (k - 0.5) * h) for k in range(1, 2 ** (i-2) + 1)))
        for j in range(2, i+1):
            r[1][j-1] = r[1][j-2] + (r[1][j-2] - r[0][j-2]) / (4 ** (j-1) - 1)
        h /= 2
        ret.append("r[" + str(i) + "]" + "[" + str(i) + "]: " + str(r[1][i-1]))
        print("n:", i, " ".join(map(lambda x: "%.8f" % x, [r[1][j] for j in range(i)])))
        if abs(r[0][i-2] - r[1][i-1]) < 1e-6:
            break
        for j in range(1, i+1):
            r[0][j-1] = r[1][j-1]
    print("\n".join(map(str, ret)))


def problem4(x):
    return exp(2 * x) * sin(3 * x)


def problem6(x):
    return cos(x) ** 2

for n in [10, 100, 1000]:
    ans = compsimpson(problem4, 0, 2, n)
    print("Simpson\t\tn: " + str(n) + "\t\t" + "%.7f" % ans)
print()

for n in [10, 100, 1000]:
    ans = comptrapezoidal(problem4, 0, 2, n)
    print("Trapezoidal\tn: " + str(n) + "\t\t" + "%.7f" % ans)

print()
print("Rhomberg")
rhomberg(problem6, -1, 1, 10)
