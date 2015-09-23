from random import randrange


def powerset(c, d=[]):
    yield d
    for i in range(len(c)):
        for s in powerset(c[i+1:], d + [c[i]]):
            yield s


def valid(c, d):
    for y in d:
        overlap = False
        for x in c:
            overlap |= (x[0] < y[1] and y[0] < x[1])
        if not overlap:
            return False

    for i in range(len(c)):
        for j in range(i+1, len(c)):
            if c[i][0] <= c[j][1] and c[j][0] <= c[i][1]:
                return False

    return True


if __name__ == "__main__":
    n = 10
    k = 1000

    c = [tuple(sorted((randrange(k), randrange(k)))) for _ in range(n)]
    s = set(c)

    for v in powerset(c):
        if valid(v, s - set(v)):
            print(v)

    print(" ".join(map(str, c)))
