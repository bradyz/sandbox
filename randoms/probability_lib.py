from math import sqrt


def mean(c):
    return sum(c) / float(len(c))


def variance(c):
    m = mean(c)
    return sum((v - m) ** 2 for v in c)


def stddev(c):
    return sqrt(variance(c) / float(len(c) - 1))


if __name__ == "__main__":
    a = [3, 5, 6, 7, 9]
    b = [2, 4, 6, 8, 10]
    print(mean(a), mean(b))
    print(stddev(a), stddev(b))

    a = [10, 14, 15, 16, 20]
    b = [10, 11, 15, 19, 20]
    print(mean(a), mean(b))
    print(stddev(a), stddev(b))
