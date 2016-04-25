def conc(init, k, t):
    print(1/(k * t + 1/init))

initial = 1.334
rate = 5.4*1e4
time = 28*1e-6
conc(initial, rate, time)


def guess(a, b, c):
    bestv = 1e9
    best = []
    bestss = list()
    for i in range(10):
        for j in range(10):
            ks = list()
            ks.append(a[2] / ((a[0] ** i) * (a[1] ** j)))
            ks.append(b[2] / ((b[0] ** i) * (b[1] ** j)))
            ks.append(c[2] / ((c[0] ** i) * (c[1] ** j)))
            ret = -1e9
            for x in range(3):
                for y in range(3):
                    ret = max(ret, abs(ks[x] - ks[y]))
            if ret < bestv:
                bestv = ret
                best = [i, j]
                bestss = ks
    print(best)
    print(bestv)
    print(bestss)

# a = [1.92, 1.36, .677]
# b = [1.92, .646, .153]
# c = [.675, 1.36, .0837]
# guess(a, b, c)

from math import exp


def first_order_conc(init, k, t):
    print(exp(-k * t) * init)

initial = .75
rate = 6.8*1e-3
time = 121
first_order_conc(initial, rate, time)
